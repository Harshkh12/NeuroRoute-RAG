
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
=======
# NeuroRoute-Rag - Intelligent Agentic AI Chatbot

[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green.svg)](https://fastapi.tiangolo.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.5.4-orange.svg)](https://python.langchain.com/langgraph/)
[![Qdrant](https://img.shields.io/badge/Qdrant-VectorDB-purple.svg)](https://qdrant.tech/)

## 📋 Overview

**NeuroRoute-Rag** is an intelligent, end-to-end Retrieval-Augmented Generation (RAG) system powered by agentic AI architecture. It combines dynamic query routing, intelligent document retrieval, and advanced LLM capabilities to provide accurate, context-aware answers to user queries.

The system intelligently adapts its retrieval strategy based on query type, utilizing indexed documents, general knowledge, or real-time web search to generate comprehensive responses. Built with a modular architecture using LangGraph for workflow orchestration and multiple storage backends for scalability.

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
=======
- **Adaptive Classification**: Automatically routes queries to the most appropriate processing pipeline
- **Three Query Types**:
  - **Index**: Queries answerable from uploaded documents
  - **General**: Queries answerable with general knowledge
  - **Search**: Queries requiring real-time web search

### 📚 Advanced RAG Pipeline
- **Document Processing**: Intelligent chunking and embedding of documents
- **Vector Search**: Fast similarity-based retrieval using Qdrant
- **Relevance Grading**: Automatic evaluation of retrieved documents
- **Query Rewriting**: Optimizes queries for better retrieval results

### 🤖 Agentic AI Architecture
- **Multi-Agent System**: Specialized agents for different tasks
- **ReAct Framework**: Reasoning and Acting pattern for intelligent decision-making
- **Tool Integration**: Seamless integration with retrieval tools and web search

### 💾 State Management
- **MongoDB Backend**: Persistent chat history and session management
- **Session Tracking**: Individual conversation contexts per user
- **Memory Management**: Full conversation context retention

### 🎨 User Interface
- **Streamlit Web App**: Interactive chat interface with document upload
- **File Support**: PDF and TXT document uploads
- **Real-time Feedback**: Live chat with instant responses

### ⚡ API-First Architecture
- **FastAPI Backend**: High-performance REST API
- **Async Operations**: Non-blocking database and API calls
- **RESTful Endpoints**: Well-defined API contracts

---

## 🏗️ Architecture

### System Components

```
┌─────────────────────────────────────────────────────────────────┐
│                         User Interface                          │
│  ┌──────────────��───────────────────────────────────────��───┐  │
│  │  Streamlit Web Application                               │  │
│  │  • Chat Interface                                        │  │
│  │  • Document Upload (PDF, TXT)                            │  │
│  │  • Session Management                                    │  │
│  └──────────────────────────────────────────────────────────��  │
└───────────────────────────────────────────��─────────────────────┘
                            ↓
┌────────────────────────────────────────────────��────────────────┐
│                       FastAPI Backend                           │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  REST API Endpoints                                      │  │
│  │  • POST /rag/query                                       │  │
│  │  • POST /rag/documents/upload                            │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│                    LangGraph Orchestration                      │
│  ┌─────────┐  ┌──────────┐  ┌─────────┐  ┌──────────┐         │
│  │ Query   │→ │ Classify │→ │ Router  │→ │ Pipeline │         │
│  │ Analyze │  │ Query    │  │ Output  │  │ Exec     │         │
│  └─────────┘  └──────────┘  └───��─────┘  └──────────┘         │
└─────────────────────────────────────────────────────────────────┘
                            ↓
        ┌───────��──────────┬────────────────��─┬────────────────┐
        ↓                  ↓                  ↓                ↓
   ┌─────────┐       ┌──────────┐      ┌────────────┐   ┌──────────┐
   │ Retriever│      │ General  │      │ Web Search │   │ Response │
   │ (Index)  │      │ LLM      │      │ (Tavily)   │   │ Generator│
   └─────────┘       └──────────┘      └────────────┘   └──────────┘
        ↓                  ↓                  ↓                ↓
        └──────────────────┬──────────────────┬────────────────┘
                           ↓
            ┌─────────────────────────────────┐
            │   Response to User               │
            └─────────────────────────────────┘
```

### Graph Nodes

1. **query_analysis**: Analyzes and classifies incoming queries
2. **retriever**: Retrieves relevant documents from vector store
3. **grade**: Evaluates relevance of retrieved documents
4. **rewrite**: Optimizes query for better retrieval results
5. **generate**: Generates final response from context
6. **web_search**: Performs real-time web search when needed
7. **general_llm**: Provides general knowledge answers


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
=======
NeuroRoute-Rag/
├── src/                              # Main source code
│   ��── main.py                       # FastAPI application entry point
│   ├── api/                          # API routes and endpoints
│   │   └── routes.py                 # RAG query and document upload endpoints
│   ├── config/                       # Configuration management
│   │   ├── settings.py               # Application settings
│   │   └── prompts.yaml              # LLM prompts and system messages
│   ├── core/                         # Core utilities
│   │   ├── config.py                 # Core configuration
│   │   └── logger.py                 # Logging setup
│   ├── db/                           # Database layer
│   │   └── mongo_client.py           # MongoDB client initialization
│   ├── llms/                         # Language model integrations
│   │   └── openai.py                 # OpenAI ChatGPT-4o initialization
│   ├── memory/                       # Chat memory management
│   │   ├── chat_history_mongo.py     # MongoDB-backed chat history
│   │   └── chathistory_in_memory.py  # In-memory chat history (fallback)
│   ├── models/                       # Data models and schemas
│   │   ├── state.py                  # Graph state definition
│   │   ├── query_request.py          # Query request schema
│   │   ├── grade.py                  # Relevance grade model
│   │   ├── route_identifier.py       # Route classification model
│   │   └── verification_result.py    # Answer verification model
│   ├── rag/                          # RAG pipeline implementation
│   │   ├── graph_builder.py          # LangGraph workflow construction
│   │   ├── nodes.py                  # Graph node implementations
│   │   ├── retriever_setup.py        # Vector store and retriever setup
│   │   ├── document_upload.py        # Document processing and upload
│   │   └── reAct_agent.py            # ReAct agent setup
│   └── tools/                        # Utility tools and functions
│       ├── common_tools.py           # Shared utility functions
│       └── graph_tools.py            # Graph routing and decision tools
│
├── streamlit_app/                    # Streamlit web application
│   ├── home.py                       # Authentication and login page
│   ├── pages/                        # Multi-page application
│   │   └── chat.py                   # Chat interface and document upload
│   └── utils/                        # Streamlit utilities
│       └── api_client.py             # Backend API client
│
├── README.md                         # This file
├── requirements.txt   
├── docs/                             # Full documentation suite
│   ├── QDRANT_SETUP.md                   # Qdrant setup guide
│   ├── DOCUMENT_UPLOAD_FLOW.md           # Document upload flow
│   └── Workflow_diagram.png              # Workflow diagram
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
=======
### Base URL
```
http://localhost:8000
```

### 1. Query Endpoint
**Process a RAG query and get intelligent response**

```http
POST /rag/query
Content-Type: application/json

{
  "query": "What is the main topic of the document?",
  "session_id": "user_session_123"
}
```

**Response:**
```json
{
  "result": {
    "type": "ai",
    "content": "Based on the document, the main topic is..."
  }
}
```

**Parameters:**
- `query` (string, required): User's question or query
- `session_id` (string, required): Unique session identifier for conversation tracking

**Status Codes:**
- `200`: Success
- `400`: Invalid request format
- `500`: Server error

---

### 2. Document Upload Endpoint
**Upload documents for RAG indexing**

```http
POST /rag/documents/upload
X-Description: Brief description of the document

Form Data:
- file: <PDF or TXT file>
```

**Response:**
```json
{
  "status": true
}
```

**Headers:**
- `X-Description` (string, required): Document description for context

**Parameters:**
- `file` (file, required): PDF or TXT file to upload (max size: depends on system)

**Supported Formats:**
- PDF (.pdf)
- Plain Text (.txt)

**Status Codes:**
- `200`: Successfully uploaded and indexed
- `400`: Invalid file type or missing description
- `500`: Processing error

---

## 📖 Usage Guide

### 1. Prerequisites

```bash
# System Requirements
- Python 3.9 or higher
- MongoDB (local or cloud)
- Qdrant vector database
- OpenAI API key
- Tavily API key (for web search)
```

### 2. Installation

```bash
# Clone the repository
git clone https://github.com/harshkh12/NeuroRoute-Rag.git
cd NeuroRoute-Rag

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Configuration

Create a `.env` file in the project root:

```env
# Gemini Configuration
GEMINI_API_KEY=your_gemini_api_key_here
# Groq Configuration
GROQ_API_KEY=your_groq_api_key_here

# Tavily Search Configuration
TAVILY_API_KEY=your_tavily_api_key_here

# Qdrant Configuration
QDRANT_URL=http://localhost:6333
QDRANT_API_KEY=your_qdrant_api_key
QDRANT_CODE_COLLECTION=code_documents
QDRANT_DOCS_COLLECTION=documents

# MongoDB Configuration
MONGODB_URL=mongodb://localhost:27017
MONGODB_DB_NAME=neuroroute_rag
```

### 4. Running the Application

**Start FastAPI Backend:**
```bash
# Terminal 1: Run FastAPI server
python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

**Start Streamlit Frontend:**
```bash
# Terminal 2: Run Streamlit app
streamlit run streamlit_app/home.py
```

**Access the Application:**
- Web Interface: http://localhost:8501
- API Documentation: http://localhost:8000/docs
- ReDoc Documentation: http://localhost:8000/redoc

### 5. Example Usage

**Using the Web Interface:**
1. Navigate to http://localhost:8501
2. Create account or login
3. Upload documents in the sidebar
4. Start chatting in the main chat area

**Using cURL:**
```bash
# Upload a document
curl -X POST http://localhost:8000/rag/documents/upload \
  -H "X-Description: Sample document about Python" \
  -F "file=@document.pdf"

# Query the RAG system
curl -X POST http://localhost:8000/rag/query \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Tell me about Python",
    "session_id": "user_123"
  }'
```

**Using Python:**
```python
import requests

# Query endpoint
response = requests.post(
    "http://localhost:8000/rag/query",
    json={
        "query": "What is Python?",
        "session_id": "user_123"
    }
)
print(response.json())
```

---

## 🔧 Configuration

### Key Configuration Files

#### `config/settings.py`
```python
# Core application settings loaded from environment
GEMINI_API_KEY           # Gemini API authentication
GROQ_API_KEY          # Groq API authentication
TAVILY_API_KEY          # Web search functionality
QDRANT_URL              # Vector database endpoint
QDRANT_API_KEY          # Vector database authentication
MONGODB_URL             # Chat history database
```

#### `config/prompts.yaml`
Contains system prompts for:
- **system_prompt**: ReAct agent system instructions
- **classify_prompt**: Query classification logic
- **grading_prompt**: Document relevance evaluation
- **rewrite_prompt**: Query optimization
- **generate_prompt**: Response generation

### Query Routing Logic

The system routes queries based on classification:

```
Query Classification
├── "index" → Use retriever (indexed documents)
├── "general" → Use general LLM (common knowledge)
└── "search" → Use web search (real-time information)
```

---

## 🧪 Testing the API

### Using FastAPI Interactive Documentation

1. Navigate to http://localhost:8000/docs
2. Expand endpoint sections
3. Click "Try it out"
4. Enter test data
5. Click "Execute"

### Example Test Cases

**Test 1: Simple Query**
```json
{
  "query": "Hello, how are you?",
  "session_id": "test_user_1"
}
```

**Test 2: Document-Based Query**
```json
{
  "query": "What topics are covered in the uploaded document?",
  "session_id": "test_user_1"
}
```

**Test 3: General Knowledge Query**
```json
{
  "query": "What is machine learning?",
  "session_id": "test_user_1"
}
```

---

## 🔐 Security Considerations

- Store API keys in `.env` file (never commit)
- Use environment variables for sensitive data
- Implement rate limiting for production
- Validate all user inputs
- Use HTTPS in production
- Implement authentication/authorization
- Secure MongoDB with proper credentials

---

## 🚀 Deployment

### Local Development
```bash
# Run development server with auto-reload
python -m uvicorn src.main:app --reload
```

### Production Deployment
```bash
# Run with production settings
python -m uvicorn src.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Docker Support (Optional)
Create `Dockerfile` and `docker-compose.yml` for containerized deployment.

---

## 📊 Performance Optimization

- **Document Chunking**: Configurable chunk size (1000 chars, 150 overlap)
- **Vector Search**: Efficient similarity search with Qdrant
- **Async Operations**: Non-blocking I/O for better throughput
- **Caching**: Query results cached when applicable
- **Batch Processing**: Document processing in batches

---

## 📚 Technology Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **LLM Framework** | LangChain | ~0.3.27 |
| **Workflow Orchestration** | LangGraph | ~0.5.4 |
| **Web Framework** | FastAPI | Latest |
| **ASGI Server** | Uvicorn | Latest |
| **UI Framework** | Streamlit | Latest |
| **Vector Database** | Qdrant/FAISS | Latest |
| **Chat Database** | MongoDB/InMemory | Latest |
| **Document Processing** | LangChain Community | ~0.3.27 |
| **LLM Provider** | OpenAI | ~0.3.28 |
| **Web Search** | Tavily | Latest |
| **Async DB** | Motor | Latest |
| **Data Validation** | Pydantic | ~2.11.7 |

