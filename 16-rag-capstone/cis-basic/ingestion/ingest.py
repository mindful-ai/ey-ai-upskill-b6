import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

# Load environment variables
load_dotenv()

keypath = r"E:\Lenovo Ideapad 330\company-material\digital-workforce-transformation\ai-upskill-5\key-vault\openai\api.key"
with open(keypath) as f:
    api_key = f.read().strip()

def ingest():
    print("\n📄 Loading CIS document...")

    loader = PyPDFLoader(r"E:\Lenovo Ideapad 330\company-material\digital-workforce-transformation\ai-upskill-5\31-rag-capstone\cis-basic\data\cis_docs\CIS_Microsoft_Windows_11_Enterprise_Benchmark_v5.0.1.pdf")
    documents = loader.load()

    print(f"✅ Loaded {len(documents)} pages")

    # Split into chunks
    print("\n✂️ Splitting into chunks...")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    print(f"✅ Created {len(chunks)} chunks")

    # Create embeddings
    print("\n🧠 Generating embeddings...")

    embeddings = OpenAIEmbeddings(api_key=api_key)

    # Create vector store
    print("\n📦 Storing in FAISS vector DB...")

    db = FAISS.from_documents(chunks, embeddings)

    # Save locally
    db.save_local("vectorstore/")

    print("\n🎉 Ingestion complete! Vector store saved.")

if __name__ == "__main__":
    ingest()