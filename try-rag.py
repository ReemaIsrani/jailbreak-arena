from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vectorstore = FAISS.load_local("vectorstore/security", embeddings=embedding_model, allow_dangerous_deserialization=True)

retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})

query = "base64"

docs = retriever.get_relevant_documents(query)

for i, doc in enumerate(docs, 1):
    print(f"\n--- Document {i} ---\n{doc.page_content}")
