import json
import os
import faiss
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.documents import Document

MEMORY_FILE = "data/memory.json"
MEMORY_INDEX_PATH = "data/memory_index"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []

def save_to_memory(problem_text, solution_text, embeddings, topic="General"):
    memories = load_memory()
    new_entry = {
        "problem": problem_text,
        "solution": solution_text,
        "topic": topic
    }
    memories.append(new_entry)
    
    with open(MEMORY_FILE, "w") as f:
        json.dump(memories, f, indent=2)
        
    rebuild_memory_index(memories, embeddings)
    return "Saved to memory!"

def rebuild_memory_index(memories, embeddings):
    if not memories:
        return
    
    documents = [
        Document(page_content=m["problem"], metadata={"solution": m["solution"]})
        for m in memories
    ]
    
    vectorstore = FAISS.from_documents(documents, embeddings)
    vectorstore.save_local(MEMORY_INDEX_PATH)

def retrieve_similar_solution(current_problem_text, embeddings):
    if not os.path.exists(MEMORY_INDEX_PATH):
        return None
        
    try:
        vectorstore = FAISS.load_local(MEMORY_INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
        docs = vectorstore.similarity_search_with_score(current_problem_text, k=1)
        
        if not docs:
            return None
            
        doc, score = docs[0]
        # FAISS L2 distance: Lower is better. 0 = exact match.
        if score < 0.3: 
            return doc.metadata["solution"]
        return None
    except Exception as e:
        print(f"Memory retrieval error: {e}")
        return None
