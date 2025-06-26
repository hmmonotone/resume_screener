import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

load_dotenv()

UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./data/resumes")
INDEX_DIR = os.getenv("INDEX_DIR", "./data/index")
API_KEY    = os.getenv("OPENAI_API_KEY")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(INDEX_DIR, exist_ok=True)

embeddings = OpenAIEmbeddings(openai_api_key=API_KEY)
if os.listdir(INDEX_DIR):
    vector_store = FAISS.load_local(INDEX_DIR, embeddings)
else:
    vector_store = FAISS.from_documents([], embeddings)


def ingest_resume(file_path: str) -> str:
    loader = PyPDFLoader(file_path)
    docs   = loader.load()
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)
    vector_store.add_documents(chunks)
    vector_store.save_local(INDEX_DIR)
    return os.path.basename(file_path)


def score_job_description(job_desc: str, top_k: int = 5):
    q_vec   = embeddings.embed_query(job_desc)
    results = vector_store.similarity_search_by_vector(q_vec, k=top_k)
    scored  = [(doc.metadata.get("source",""), 1 - doc.score) for doc in results]
    return scored