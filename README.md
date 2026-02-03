# 📡 Telecom Knowledge Assistant (RAG + Endee)

## 📌 Overview

This project is a **Retrieval-Augmented Generation (RAG)** based Telecom Knowledge Assistant.
It answers telecom and networking-related questions using **semantic search** over
domain-specific documents instead of generic internet data.

The system demonstrates how **vector databases like Endee** can be used in AI applications
for efficient information retrieval.

---

## 🎯 Problem Statement

Traditional keyword-based search systems fail to understand the meaning of user queries.
This project solves the problem by:

- Converting telecom documents into vector embeddings
- Performing semantic similarity search
- Generating context-aware answers from retrieved content

---

## 🏗️ System Architecture

1. Telecom documents are stored as text files
2. Documents are converted into embeddings using Sentence Transformers
3. Embeddings are stored in an **Endee-compatible vector format**
4. User queries are embedded and matched using cosine similarity
5. Relevant context is retrieved
6. A local generation layer produces a focused answer
7. Results are displayed using a Streamlit web interface

---

## 🧠 Technologies Used

- Python
- Sentence Transformers
- Endee (Vector Database – conceptual integration)
- NumPy
- Streamlit
- Git & GitHub

---

## 📂 Project Structure

telecom-rag-endee/
│
├── app.py # Streamlit UI
├── ingest.py # Document ingestion & embedding
├── search.py # Semantic search & RAG logic
├── data/ # Telecom knowledge files
├── README.md
├── requirements.txt
└── vectors.pkl # Generated vector store

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/MaheshPreddy/telecom-rag-endee.git
cd telecom-rag-endee

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Ingest data
python ingest.py

5️⃣ Run the application
streamlit run app.py

❓ Example Questions

What is TCP?

What is UDP?

What is DNS?

Explain the OSI model

Difference between 4G and 5G
```
