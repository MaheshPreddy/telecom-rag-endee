import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

VECTOR_STORE = "vectors.pkl"

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_context(query, top_k=1):
    with open(VECTOR_STORE, "rb") as f:
        vector_db = pickle.load(f)

    query_vec = model.encode([query])[0]

    scores = []
    for item in vector_db:
        score = np.dot(query_vec, item["vector"]) / (
            np.linalg.norm(query_vec) * np.linalg.norm(item["vector"])
        )
        scores.append((score, item["text"]))

    scores.sort(reverse=True)
    return scores[:top_k][0][1]

def generate_answer(question, context):
    """
    Simple local answer generation:
    - Finds sentences related to keywords in the question
    """
    keywords = question.lower().split()
    sentences = context.split(".")

    relevant = []
    for s in sentences:
        for k in keywords:
            if k in s.lower():
                relevant.append(s.strip())
                break

    if not relevant:
        return context.strip()

    return ". ".join(relevant) + "."

if __name__ == "__main__":
    question = input("Ask a question: ")
    context = retrieve_context(question)
    answer = generate_answer(question, context)

    print("\nAnswer:\n")
    print(answer)

