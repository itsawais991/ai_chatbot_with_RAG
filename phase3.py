import streamlit as st

# Phase 2 libraries
import os
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Phase 3 libraries
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA


st.title("RAG CHATBOT!")  # ✅ Correct

# session variable to store history(all old messages)
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display all the historical messages
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])    

@st.cache_resource
def get_vectorstore():
    pdf_name = "./python.pdf"
    loaders = [PyPDFLoader(pdf_name)]
    # Create chunks, aka vector database–Chromadb
    index = VectorstoreIndexCreator(
        embedding=HuggingFaceEmbeddings(model_name='all-MiniLM-L12-v2'),
        text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    ).from_loaders(loaders)
    return index.vectorstore

prompt = st.chat_input("pass your prompt here!")

if prompt:
    st.chat_message("user").markdown(prompt)  # ✅ valid role
    st.session_state.messages.append({'role': 'user', 'content': prompt})

    groq_sys_prompt = ChatPromptTemplate.from_template("""You are very smart at everything, you always give the best, 
                                            the most accurate and most precise answers. Answer the following Question: {user_prompt}.
                                            Start the answer directly. No small talk please""")

    model="llama-3.1-8b-instant"
    groq_chat = ChatGroq(
        groq_api_key="apikey",  # Add your API key here
        model_name=model
    )
    
    try:
        vectorstore = get_vectorstore()
        if vectorstore is None:
            st.error("Failed to load document")

        chain = RetrievalQA.from_chain_type(
            llm=groq_chat,
            chain_type='stuff',
            retriever=vectorstore.as_retriever(search_kwargs={'k': 3}),
            return_source_documents=True)        

        result = chain({"query": prompt})
        response = result["result"]  # Extract just the answer

        st.chat_message("Assistant").markdown(response)
        st.session_state.messages.append({'role': 'Assistant', 'content': response})

    except Exception as e:
        st.error(f"Error: {str(e)}")