import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import CharacterTextSplitter

VECTOR_STORE_PATH = "data/faiss_index"

def get_embeddings():
    # Use a small, fast local model. 
    # all-MiniLM-L6-v2 is standard for this.
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def build_vectorstore():
    """
    Reads markdown files from data/knowledge_base, chunks them, 
    and saves a FAISS index locally.
    """
    if not os.path.exists("data/knowledge_base"):
        os.makedirs("data/knowledge_base", exist_ok=True)
        return "No knowledge base directory found."

    # Load documents
    loader = DirectoryLoader("data/knowledge_base", glob="**/*.md", loader_cls=TextLoader)
    documents = loader.load()
    
    if not documents:
        return "No documents found in data/knowledge_base."

    # Split text
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)

    # Embed and store
    embeddings = get_embeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)
    
    # Save to disk
    vectorstore.save_local(VECTOR_STORE_PATH)
    return f"Vector store built with {len(chunks)} chunks."

def get_retriever():
    """
    Returns a retriever object that can be used in a LangChain chain.
    """
    embeddings = get_embeddings()
    
    if not os.path.exists(VECTOR_STORE_PATH):
        # If index doesn't exist, build it first
        print("Index not found. Building...")
        res = build_vectorstore()
        print(res)

    vectorstore = FAISS.load_local(VECTOR_STORE_PATH, embeddings, allow_dangerous_deserialization=True)
    return vectorstore.as_retriever(search_kwargs={"k": 3})

def retrieve_context(query):
    """
    Simple helper to get string context for a query.
    """
    retriever = get_retriever()
    docs = retriever.invoke(query)
    return "\n\n".join([d.page_content for d in docs])
