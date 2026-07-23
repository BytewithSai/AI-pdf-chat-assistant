import os
import tempfile
import time

import streamlit as st

from utils.loader import load_pdf
from utils.splitter import split_documents
from utils.embeddings import create_vector_store
from utils.retriever import get_retriever
from utils.chain import build_chain

st.set_page_config(
    page_title="AI PDF Chat Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI PDF Chat Assistant")
st.markdown(
    "<span style='color:gray;'>Upload a PDF and ask questions about its contents.</span>",
    unsafe_allow_html=True,
)

# -------------------------
# Session State
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chain" not in st.session_state:
    st.session_state.chain = None

if "pdf_name" not in st.session_state:
    st.session_state.pdf_name = None

if "pages" not in st.session_state:
    st.session_state.pages = 0

if "chunks" not in st.session_state:
    st.session_state.chunks = 0

st.divider()

# -------------------------
# Sidebar
# -------------------------
with st.sidebar:

    st.header("📂 Upload Document")

    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"],
        help="Upload a PDF to start chatting with it."
    )

    if uploaded_file:

        if uploaded_file.name != st.session_state.pdf_name:

            # Reset previous session
            st.session_state.messages = []
            st.session_state.chain = None
            st.session_state.pages = 0
            st.session_state.chunks = 0

            # Progress UI
            progress = st.progress(0)
            status = st.empty()

            # Save PDF
            status.info("📄 Saving uploaded PDF...")
            progress.progress(10)

            

            os.makedirs("data", exist_ok=True)

            pdf_path = "data/current.pdf"

            with open(pdf_path, "wb") as f:
                f.write(uploaded_file.getvalue())

            # Load PDF
            status.info("📖 Loading PDF...")
            progress.progress(25)

            documents = load_pdf(pdf_path)

            # Split document
            status.info("✂️ Splitting document into chunks...")
            progress.progress(45)

            chunks = split_documents(documents)

            # Create embeddings
            status.info("🧠 Creating embeddings...")
            progress.progress(70)

            print("➡️ Creating Vector Store...")
            vector_store = create_vector_store(chunks)
            print("✅ Vector Store Created")

            # Build retriever
            status.info("🔍 Building retriever...")
            progress.progress(85)

            retriever = get_retriever(vector_store)

            # Build chain
            status.info("🤖 Preparing AI assistant...")
            progress.progress(95)

            chain = build_chain(retriever)

            st.session_state.chain = chain
            st.session_state.pdf_name = uploaded_file.name
            st.session_state.pages = len(documents)
            st.session_state.chunks = len(chunks)
            st.session_state.messages = []

            # Finish
            progress.progress(100)
            status.success("✅ PDF processed successfully!")

            time.sleep(1.0)

            progress.empty()
            status.empty()

    st.divider()

    st.subheader("📄 Current PDF")

    if st.session_state.pdf_name:

        st.success(f"**{st.session_state.pdf_name}**")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Pages", st.session_state.pages)

        with col2:
            st.metric("Chunks", st.session_state.chunks)

        st.success("✅ Ready to chat")

    else:

        st.info("Upload a PDF to begin.")

    st.divider()

    if st.button(
        "🗑 Clear Chat",
        use_container_width=True
    ):
        st.session_state.messages = []

    st.divider()

    st.caption("Built with ❤️ using Streamlit + LangChain + Groq")

# -------------------------
# Chat History
# -------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------
# Chat Input
# -------------------------
prompt = st.chat_input("Ask something about your PDF...")

if prompt:

    if st.session_state.chain is None:
        st.warning("Please upload a PDF first.")
        st.stop()

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("🤖 Thinking..."):
            response = st.session_state.chain.invoke(prompt)

        placeholder = st.empty()

        full_response = ""

        for char in response:

            full_response += char

            placeholder.markdown(full_response + "▌")

            time.sleep(0.015)

        placeholder.markdown(full_response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )