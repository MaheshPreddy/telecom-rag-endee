# import pickle
# import numpy as np
# import streamlit as st
# from sentence_transformers import SentenceTransformer

# VECTOR_STORE = "vectors.pkl"

# model = SentenceTransformer("all-MiniLM-L6-v2")

# def retrieve_context(query):
#     with open(VECTOR_STORE, "rb") as f:
#         vector_db = pickle.load(f)

#     query_vec = model.encode([query])[0]

#     scores = []
#     for item in vector_db:
#         score = np.dot(query_vec, item["vector"]) / (
#             np.linalg.norm(query_vec) * np.linalg.norm(item["vector"])
#         )
#         scores.append((score, item["text"]))

#     scores.sort(reverse=True)
#     return scores[0][1]

# def generate_answer(question, context):
#     keywords = question.lower().split()
#     sentences = context.split(".")

#     relevant = []
#     for s in sentences:
#         for k in keywords:
#             if k in s.lower():
#                 relevant.append(s.strip())
#                 break

#     if not relevant:
#         return context.strip()

#     return ". ".join(relevant) + "."

# st.title("📡 Telecom Knowledge Assistant (RAG + Endee)")

# question = st.text_input("Ask a telecom or networking question:")

# if question:
#     context = retrieve_context(question)
#     answer = generate_answer(question, context)

#     st.subheader("Answer")
#     st.write(answer)


import streamlit as st
from search import search_answer   

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Telecom Knowledge Assistant",
    page_icon="📡",
    layout="centered"
)

# ---------------- HEADER ----------------
st.markdown(
    """
    <h1 style="text-align:center;">📡 Telecom Knowledge Assistant</h1>
    <p style="text-align:center; font-size:18px;">
    Retrieval-Augmented Generation (RAG) using Endee Vector Database
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("📘 Project Info")
    st.markdown(
        """
        **Domain:** Telecom & Networking  
        **Technique:** Semantic Search + RAG  
        **Vector DB:** Endee (compatible)  
        **UI:** Streamlit  
        """
    )

    st.markdown("---")
    st.subheader("💡 Example Questions")
    st.markdown(
        """
        - What is TCP?
        - What is UDP?
        - What is DNS?
        - Explain OSI model
        - Difference between 4G and 5G
        """
    )

# ---------------- MAIN INPUT ----------------
st.subheader("🧠 Ask a Telecom Question")

query = st.text_input(
    "Enter your question:",
    placeholder="e.g., What is TCP and how is it different from UDP?"
)

# ---------------- SEARCH & ANSWER ----------------
if query:
    with st.spinner("🔍 Searching relevant telecom knowledge..."):
        answer = search_answer(query)

    st.markdown("### 📄 Answer")
    st.success(answer)

# ---------------- FOOTER ----------------
st.markdown(
    """
    <hr>
    <p style="text-align:center; font-size:14px;">
    Built by Mahesh P | AI + Vector Search Project
    </p>
    """,
    unsafe_allow_html=True
)
