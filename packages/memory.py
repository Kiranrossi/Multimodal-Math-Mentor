import json
import os
import faiss
import numpy as np
from langchain_community.vectorstores import FAISS # type: ignore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

MEMORY_FILE = "data/memory.json"
MEMORY_INDEX_PATH = "data/memory_index"

def get_embeddings():
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def load_memory():
    """Load the raw JSON memory."""
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []

def save_to_memory(problem_text, solution_text, topic):
    """
    Saves a verified problem-solution pair to JSON and updates the FAISS index.
    """
    # 1. Save to JSON
    memories = load_memory()
    new_entry = {
        "problem": problem_text,
        "solution": solution_text,
        "topic": topic
    }
    memories.append(new_entry)
    
    with open(MEMORY_FILE, "w") as f:
        json.dump(memories, f, indent=2)
        
    # 2. Update Vector Index (for retrieval)
    # Ideally we'd add to existing index, but rebuilding is safer/easier for small scale
    rebuild_memory_index(memories)
    return "Saved to memory!"

def rebuild_memory_index(memories):
    """Rebuilds the FAISS index from the memory list."""
    if not memories:
        return
    
    documents = [
        Document(page_content=m["problem"], metadata={"solution": m["solution"]})
        for m in memories
    ]
    
    embeddings = get_embeddings()
    vectorstore = FAISS.from_documents(documents, embeddings)
    vectorstore.save_local(MEMORY_INDEX_PATH)

def retrieve_similar_solution(current_problem_text):
    """
    Checks if we have solved a similar problem before.
    Returns the solution if a close match is found, else None.
    """
    if not os.path.exists(MEMORY_INDEX_PATH):
        return None
        
    embeddings = get_embeddings()
    try:
        vectorstore = FAISS.load_local(MEMORY_INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
        # Search for top 1 document
        docs = vectorstore.similarity_search_with_score(current_problem_text, k=1)
        
        if not docs:
            return None
            
        doc, score = docs[0]
        # FAISS L2 distance: Lower is better. 0 = exact match.
        # Threshold: < 0.3 implies very similar.
        if score < 0.3: 
            return doc.metadata["solution"]
        return None
    except Exception as e:
        print(f"Memory retrieval error: {e}")
        return None
