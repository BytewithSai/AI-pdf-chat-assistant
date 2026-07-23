import os
import shutil

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


VECTOR_STORE_PATH = "vector_store"


def create_vector_store(chunks):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    if os.path.exists(VECTOR_STORE_PATH):
        shutil.rmtree(VECTOR_STORE_PATH)

    os.makedirs(VECTOR_STORE_PATH, exist_ok=True)

    vector_store.save_local(VECTOR_STORE_PATH)

    print(f"✅ FAISS index saved to: {os.path.abspath(VECTOR_STORE_PATH)}")

    return vector_store