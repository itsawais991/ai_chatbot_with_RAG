import streamlit as st

# Phase 2 libraries
import os
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

st.title("RAG CHATBOT!")  # ✅ Correct

# session variable to store history(all old messages)
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display all the historical messages
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])    
 
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
   # groq_chat = ChatGroq(
    #    groq_api_key = os.environ.get("GROQ_API_KEY"),
     #   model_name = model
    #)

    chain = groq_sys_prompt | groq_chat | StrOutputParser()
    response = chain.invoke({"user_prompt": prompt})


    #response = "I am your Assistant!"
    st.chat_message("Assistant").markdown(response)
    st.session_state.messages.append({'role': 'Assistant', 'content': response})
