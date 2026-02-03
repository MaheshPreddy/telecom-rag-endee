import os
import pickle
from sentence_transformers import SentenceTransformer

DATA_DIR = "data"
VECTOR_STORE = "vectors.pkl"

model = SentenceTransformer("all-MiniLM-L6-v2")

def load_documents():
    docs = []
    for file in os.listdir(DATA_DIR):
        if file.endswith(".txt"):
            with open(os.path.join(DATA_DIR, file), "r", encoding="utf-8") as f:
                docs.append(f.read())
    return docs

def ingest():
    documents = load_documents()
    embeddings = model.encode(documents)

    vector_db = []
    for i, emb in enumerate(embeddings):
        vector_db.append({
            "id": i,
            "vector": emb,
            "text": documents[i]
        })

    with open(VECTOR_STORE, "wb") as f:
        pickle.dump(vector_db, f)

    print("✅ Documents embedded and stored (Endee-compatible vector format)")

if __name__ == "__main__":
    ingest()
