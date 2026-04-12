# 🧠 NeuroRoute-RAG: Self-Improving Hybrid Agentic RAG System

[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green.svg)](https://fastapi.tiangolo.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Agentic-orange.svg)](https://python.langchain.com/langgraph/)
[![Qdrant](https://img.shields.io/badge/Qdrant-VectorDB-purple.svg)](https://qdrant.tech/)

---

## 🚀 Overview

**NeuroRoute-RAG** is a production-style, self-improving Retrieval-Augmented Generation (RAG) system built with an agentic AI architecture.

It goes beyond traditional RAG by integrating:

* 🔍 **Hybrid Retrieval (Dense + Sparse + Web)**
* 🧩 **Context Compression for efficient LLM usage**
* 🔁 **Feedback-driven learning loop**
* 🤖 **Dynamic LLM routing (Gemini + Groq)**

The system intelligently adapts retrieval strategies, optimizes context, and continuously improves response quality based on user interactions.

---

## 💡 Highlights

* Self-improving RAG with feedback-based adaptation
* Hybrid retrieval combining vector search, keyword matching, and web search
* Context-aware compression to reduce tokens & improve relevance
* Multi-agent orchestration using LangGraph
* Cost-optimized LLM routing (Gemini + Groq)
* Modular, production-ready architecture

---

## 🎯 Key Features

### 🧠 Intelligent Query Routing

* Classifies queries into:

  * **Index-based**
  * **General knowledge**
  * **Real-time search**
* Routes dynamically to optimal pipeline

---

### 🔍 Hybrid Retrieval System

* **Dense Retrieval** → Qdrant (vector similarity)
* **Sparse Retrieval** → BM25-style keyword matching
* **Web Search** → Tavily API

👉 Combines and reranks results for better recall & accuracy

---

### 🧩 Context Compression Layer

* Filters irrelevant chunks
* Summarizes retrieved documents
* Reduces token usage & latency
* Improves answer precision

---

### 🔁 Self-Improving Feedback Loop

* Collects user feedback (👍 / 👎)
* Stores:

  * Query
  * Retrieved documents
  * Response
* Adapts:

  * Retrieval depth
  * Routing decisions
  * Response generation

---

### 🤖 Agentic AI Architecture

* Built with LangGraph
* Uses ReAct-style reasoning
* Modular agent-based execution

---

### ⚡ Dynamic LLM Routing

* **Groq (LLaMA / Mixtral)** → Fast responses
* **Gemini** → Better reasoning

👉 Selects model based on query complexity

---

### 💾 State & Memory Management

* MongoDB-backed chat history
* Session-level context tracking
* Persistent conversation memory

---

### 🎨 User Interface

* Streamlit-based chat interface
* Document upload support (PDF, TXT)
* Real-time responses + feedback buttons

---

## 🏗️ System Architecture

```
User Query
   ↓
Query Analyzer (Intent + Complexity)
   ↓
Adaptive Router
   ↓
Hybrid Retrieval
 (Dense + Sparse + Web)
   ↓
Relevance Grading + Reranking
   ↓
Context Compression
   ↓
LLM (Gemini / Groq)
   ↓
Response Generation
   ↓
Feedback Collector
   ↓
Adaptive Learning Loop
```

---

## 🧩 Core Components

### Graph Nodes

* `query_analysis` → classify query
* `router` → decide pipeline
* `retriever` → hybrid retrieval
* `grade` → relevance scoring
* `rewrite` → query optimization
* `compression` → context summarization
* `generate` → response generation
* `feedback` → learning loop

---

## 📦 Project Structure

```
NeuroRouteRAG/
├── src/
│   ├── api/                 # FastAPI routes
│   ├── config/              # Settings & prompts
│   ├── core/                # Logging & config
│   ├── db/                  # MongoDB integration
│   ├── llms/                # Gemini + Groq wrappers
│   ├── memory/              # Chat history
│   ├── models/              # Pydantic schemas
│   ├── rag/
│   │   ├── graph_builder.py
│   │   ├── nodes.py
│   │   ├── retriever_setup.py
│   │   ├── sparse_retriever.py
│   │   ├── context_compressor.py
│   │   └── reAct_agent.py
│   └── tools/               # Utility tools
│
├── streamlit_app/           # UI
├── README.md
├── requirements.txt
```

---

## 🔌 API Endpoints

### ➤ Query

```http
POST /rag/query
```

```json
{
  "query": "Explain transformers",
  "session_id": "user_123"
}
```

---

### ➤ Feedback

```http
POST /rag/feedback
```

```json
{
  "query": "...",
  "response": "...",
  "feedback": 1
}
```

---

### ➤ Document Upload

```http
POST /rag/documents/upload
```

---

## ⚙️ Setup & Installation

### 1. Clone Repo

```bash
git clone https://github.com/your-username/neuroroute-rag.git
cd neuroroute-rag
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Environment Variables

```env
# LLM APIs
GEMINI_API_KEY=your_key
GROQ_API_KEY=your_key

# Vector DB
QDRANT_URL=http://localhost:6333

# Database
MONGODB_URL=mongodb://localhost:27017

# Web Search
TAVILY_API_KEY=your_key
```

---

### 4. Run Backend

```bash
uvicorn src.main:app --reload
```

---

### 5. Run Frontend

```bash
streamlit run streamlit_app/home.py
```

---

## 📊 Performance Optimizations

* Hybrid retrieval improves recall
* Context compression reduces token usage
* Async FastAPI for high throughput
* LLM routing for cost optimization
* Feedback loop improves long-term accuracy

---

## 🔐 Security

* API keys via environment variables
* Input validation using Pydantic
* Secure DB connections
* Rate limiting (recommended for production)

---

## 🧪 Future Improvements

* 📊 LLM evaluation dashboard
* 🧠 Prompt optimization engine
* 🎥 Multimodal support (image/video)
* 📉 Cost & latency tracking
* 🔍 Hallucination detection
