import os
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import CharacterTextSplitter
from models.embeddings import get_embeddings_model
from config.config import VECTOR_STORE_PATH

def build_vectorstore():
    if not os.path.exists("data/knowledge_base"):
        os.makedirs("data/knowledge_base", exist_ok=True)
        return "No knowledge base directory found."

    loader = DirectoryLoader("data/knowledge_base", glob="**/*.md", loader_cls=TextLoader)
    documents = loader.load()
    
    if not documents:
        return "No documents found in data/knowledge_base."

    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)

    embeddings = get_embeddings_model()
    vectorstore = FAISS.from_documents(chunks, embeddings)
    
    vectorstore.save_local(VECTOR_STORE_PATH)
    return f"Vector store built with {len(chunks)} chunks."

def get_retriever():
    embeddings = get_embeddings_model()
    
    if not os.path.exists(VECTOR_STORE_PATH):
        print("Index not found. Building...")
        res = build_vectorstore()
        print(res)

    vectorstore = FAISS.load_local(VECTOR_STORE_PATH, embeddings, allow_dangerous_deserialization=True)
    return vectorstore.as_retriever(search_kwargs={"k": 3})

def retrieve_context(query):
    try:
        retriever = get_retriever()
        docs = retriever.invoke(query)
        return "\n\n".join([d.page_content for d in docs])
    except Exception as e:
        return ""
