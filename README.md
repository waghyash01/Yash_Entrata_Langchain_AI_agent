# 🤖 AI-Powered Knowledge Quiz Builder (RAG + Agentic AI System)

## 👤 Submission Details

- **Candidate:**   Yash Dattatray Wagh  
- **Email:**       yashdwagh01@gmail.com  
- **College:**     PCCOE  

---

## 📌 Overview

The AI Quiz Builder is a full-stack intelligent quiz generation system that transforms any user-provided topic into a structured, interactive assessment using Generative AI, Retrieval-Augmented Generation (RAG), and semantic search.

This project goes beyond a basic LLM wrapper — it implements a complete **AI learning pipeline with retrieval, reasoning, evaluation, and persistence layers.**

---

## 🌟 What Makes This Project Stand Out

This system is not just an AI quiz generator — it is a **mini AI learning assistant platform** with:

- 🧠 Retrieval-Augmented Generation (RAG) pipeline  
- 📚 Wikipedia-powered dynamic knowledge retrieval  
- ⚡ FAISS vector database for semantic context search  
- 🤖 Structured output generation using LLM + Pydantic models  
- 💬 Real-time interactive quiz engine (Streamlit UI)  
- 📊 Automatic evaluation + scoring system  
- 🧾 Persistent quiz history tracking  
- 🔄 Multi-layer fallback handling for robustness  

---

## 🏗️ System Architecture
User Input (Topic)
↓
Wikipedia API (Knowledge Retrieval Layer)
↓
FAISS Vector Store (Semantic Search Layer)
↓
LangChain Orchestration Layer
↓
Gemini LLM (Structured Quiz Generation)
↓
Pydantic Schema Validation
↓
Streamlit UI (Interactive Quiz Interface)
↓
Evaluation Engine (Scoring + Feedback)
↓
Persistent History Storage (File-based Logging)


---

## ⚙️ Key Technical Decisions

### 1. LangChain Orchestration
Used to connect LLM, retriever, and structured output pipelines into a modular and scalable AI workflow.

### 2. Gemini 1.5 Flash Model
Chosen for:
- Low latency generation  
- Strong reasoning for educational content  
- Free-tier accessibility  

### 3. FAISS Vector Store
Implemented for semantic retrieval over Wikipedia context to improve factual grounding of generated questions.

### 4. Wikipedia as Knowledge Source (RAG Layer)
Used as a lightweight, real-time external knowledge base for dynamic topic expansion.

### 5. Pydantic Structured Output
Ensures strict validation for:
- Questions  
- Options (A–D)  
- Correct answers  
- Explanations  

This eliminates invalid or hallucinated outputs.

### 6. Streamlit Frontend
Provides:
- Interactive quiz UI  
- Real-time scoring  
- History tracking  
- Clean UX for fast interaction  

---

## 🧠 Advanced Features (Bonus Implementations)

### 🔹 Retrieval-Augmented Generation (RAG)
Wikipedia + FAISS-based semantic retrieval improves factual accuracy of quiz generation.

### 🔹 Robust Error Handling
- Wikipedia disambiguation handling  
- Empty context fallback  
- API quota-safe execution  

### 🔹 Persistent Quiz Memory
Stores:
- Questions  
- User answers  
- Correct answers  
- Score  
- Feedback  

### 🔹 Evaluation Engine
Provides:
- Auto scoring  
- Answer-wise feedback  
- Performance summary  

### 🔹 Streamlit Session Optimization
Prevents unnecessary re-execution and improves UI performance.

---

## 🔁 End-to-End Flow

1. User enters topic  
2. Wikipedia retrieves relevant knowledge  
3. FAISS indexes & retrieves semantic context  
4. LangChain combines prompt + context  
5. Gemini generates structured quiz  
6. Streamlit renders interactive UI  
7. User submits answers  
8. System evaluates performance  
9. Results stored in history  

---

## 🚀 Outcome

This project demonstrates:
- End-to-end AI system design  
- Real-world RAG implementation  
- LangChain-based orchestration  
- Production-style UI design  
- Clean modular architecture  

---

## 🧰 Tech Stack

- Python  
- LangChain  
- Google Gemini API  
- FAISS Vector Database  
- Wikipedia API  
- Streamlit  
- Pydantic  
- dotenv  

---

## 📌 Summary

This is a production-grade AI quiz system combining retrieval, generation, evaluation, and persistence into a single unified architecture, demonstrating strong understanding of modern LLM application engineering.
