from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from langchain_groq import ChatGroq

from config import GROQ_API_KEY


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def build_chain(retriever):

    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama-3.3-70b-versatile"
    )

    prompt = ChatPromptTemplate.from_template(
    """
You are an AI PDF Chat Assistant.

Answer the user's question ONLY from the provided PDF context.

Rules:
- Do not use your own knowledge.
- Do not make up information.
- If the answer is not found in the context, reply exactly:
  "I couldn't find that information in the uploaded PDF."

Context:
{context}

Question:
{question}

Answer:
"""
)

    chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain