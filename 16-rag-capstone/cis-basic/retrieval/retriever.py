from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings


from dotenv import load_dotenv
load_dotenv()

keypath = r"E:\Lenovo Ideapad 330\company-material\digital-workforce-transformation\ai-upskill-5\key-vault\openai\api.key"
with open(keypath) as f:
    api_key = f.read().strip()

def get_retriever():
    embeddings = OpenAIEmbeddings(api_key=api_key)

    db = FAISS.load_local(
        "vectorstore/",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = db.as_retriever(
        search_kwargs={"k": 10}  # top 4 chunks
    )

    return retriever