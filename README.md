# 🤖 AI PDF Chat Assistant

An AI-powered PDF Chat Assistant that allows users to upload a PDF and ask natural language questions about its contents. The application uses Retrieval-Augmented Generation (RAG) to provide accurate answers grounded in the uploaded document.

## 🚀 Live Demo

https://ai-pdf-chat-assistant-q5xzgezuaknbnxkgg5yxg9.streamlit.app/

---


## ✨ Features

- 📄 Upload PDF documents
- 💬 Chat with your PDF using natural language
- 🧠 Retrieval-Augmented Generation (RAG)
- 🔍 Semantic search using FAISS
- 🤖 Powered by Groq Llama 3.3 70B
- ⚡ Character-by-character response animation
- 📊 PDF processing progress indicator
- 📑 Page and chunk statistics
- 🔄 Automatic reset when a new PDF is uploaded
- 🧹 Clear chat functionality
- 🎨 Clean and responsive Streamlit interface

---

## 🏗️ Tech Stack

- Python
- Streamlit
- LangChain
- Groq API
- FAISS
- HuggingFace Embeddings
- Sentence Transformers
- PyPDF
- Recursive Character Text Splitter

---

## 📂 Project Structure

```text
AI-pdf-chat-assistant/
│
├── app.py
├── config.py
├── requirements.txt
├── .gitignore
│
├── utils/
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── retriever.py
│   └── chain.py
│
└── data/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/BytewithSai/AI-pdf-chat-assistant.git
```

Move into the project directory

```bash
cd AI-pdf-chat-assistant
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
```

Run the application

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. Upload a PDF.
2. The PDF is loaded using PyPDFLoader.
3. The document is split into chunks.
4. HuggingFace Embeddings generate vector representations.
5. FAISS stores and retrieves relevant chunks.
6. LangChain builds the retrieval pipeline.
7. Groq Llama 3.3 generates answers based only on the retrieved context.
8. Responses are displayed in a ChatGPT-like interface.

---

## 🎯 Future Improvements

- 📄 Source page citations
- 🌙 Dark/Light theme toggle
- 📁 Multiple PDF support
- 💾 Persistent vector database
- 📊 Response time analytics
- 🔄 Re-index button
- 📥 Chat export
- 🌍 Multi-language support

---

## 👨‍💻 Author

**Sai Prakash Reddy**

GitHub: https://github.com/BytewithSai

LinkedIn: www.linkedin.com/in/saiprakashreddy1

---

## ⭐ If you found this project useful

Please consider giving it a ⭐ on GitHub!