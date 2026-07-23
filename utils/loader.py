from langchain_community.document_loaders import PyPDFLoader


def load_pdf(pdf_path):
    """
    Load a PDF and return a list of LangChain Document objects.
    """

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    return documents