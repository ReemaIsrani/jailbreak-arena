from langchain_community.vectorstores import FAISS
from langchain.agents import tool
from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.load_local("vectorstore/security", embeddings = embedding_model, allow_dangerous_deserialization=True)

@tool
def search(query: str) -> str:
    """Search the security document"""
    results = vectorstore.similarity_search(query, k=5)
    if not results:
        return f"No relevant results found."
    return "\n".join([doc.page_content for doc in results])