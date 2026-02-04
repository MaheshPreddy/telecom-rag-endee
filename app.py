
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
