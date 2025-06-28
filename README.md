RAG Chatbot with Streamlit and LangChain
🚀 A Retrieval-Augmented Generation (RAG) chatbot powered by Groq (Llama 3.1 8B), LangChain, and Streamlit. This app allows users to query a PDF document using natural language and get AI-generated responses.

📌 Features
✅ PDF Document Processing – Upload and extract text from PDFs
✅ Vector Embeddings – Uses all-MiniLM-L12-v2 for semantic search
✅ RAG Pipeline – RetrievalQA with Groq's fast LLM
✅ Chat Interface – Streamlit-based interactive UI
✅ Session Memory – Remembers conversation history

⚙️ Setup
Prerequisites
Python 3.10+

Groq API Key (Free tier available)

Installation
Clone the repository

sh
git clone https://github.com/yourusername/rag-chatbot.git
cd rag-chatbot
Install dependencies

sh
pip install -r requirements.txt
Set up environment variables
Create a .env file and add your Groq API key:

text
GROQ_API_KEY="your_api_key_here"
Add a PDF
Place your PDF in the project folder and update pdf_name in app.py.

🚀 Running the App
sh
streamlit run app.py
The app will open in your browser at http://localhost:8501.

🛠️ Customization
Changing the LLM
Replace model="llama-3.1-8b-instant" with other Groq-supported models:

mixtral-8x7b-32768

gemma-7b-it

Modifying the Prompt
Edit the groq_sys_prompt in app.py:

python
groq_sys_prompt = ChatPromptTemplate.from_template("""
    You are a helpful assistant. Answer concisely: {user_prompt}.
""")
Adjusting Chunk Size
Modify RecursiveCharacterTextSplitter parameters:

python
text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,  # Increase for larger docs
    chunk_overlap=100  # Helps maintain context
)
📂 Project Structure
text
.
├── app.py                # Main Streamlit application
├── requirements.txt      # Python dependencies
├── .env                  # API keys (gitignored)
└── your_document.pdf     # Sample PDF for testing
📜 License
MIT License – Free for personal and commercial use.

🙌 Credits
LangChain – RAG framework

Groq – Ultra-fast LLM inference

Streamlit – Web app deployment

🛠 Need help? Open an issue or contribute!
🔗 Live Demo: [Coming Soon]
