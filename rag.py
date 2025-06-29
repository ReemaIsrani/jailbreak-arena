import sys
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

def main(input_file, output_dir):
    # Load the input document
    with open(input_file, "r", encoding="utf-8") as f:
        full_text = f.read()

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    chunks = splitter.create_documents([full_text])

    # Initialize embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Create FAISS index
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # Save FAISS index to specified directory
    vectorstore.save_local(output_dir)
    print(f"FAISS index saved to: {output_dir}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_faiss_index.py <input_txt_file> <output_dir>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    main(input_path, output_path)
