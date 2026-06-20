# 🎯 Placement Intelligence Assistant

An AI-powered **Placement Intelligence System** built using **Hybrid RAG (ChromaDB + Semantic Search), Tool-Augmented Reasoning, Groq Llama 3.1, and Streamlit** that answers placement-related queries with accurate, grounded responses.

---

## 📌 Overview

Placement Intelligence Assistant helps students quickly access placement-related information using natural language queries.

It can answer:
- Company CGPA cutoffs  
- Hiring trends  
- Interview experiences  
- Package analysis  
- Tech industry updates  
- General queries (via tools like web search, calculator, date)

---

## 🎯 Project Goal

To build an intelligent AI assistant that:

- Understands natural language queries
- Automatically routes queries (Tool vs RAG)
- Retrieves accurate information from dataset
- Reduces hallucinations using grounding
- Tracks analytics (top + recent questions)
- Evaluates system using RAGAS metrics

---

## 🔄 Simple Workflow (Easy Understanding)

```

User Question
↓
Streamlit UI
↓
Query Router
┌───────────────┬────────────────┬───────────────┐
│ Date Query    │ Calculator     │ Web Search    │
└───────────────┴────────────────┴───────────────┘
↓
RAG Pipeline
↓
ChromaDB Retriever
↓
Relevant Context
↓
Llama 3.1 (Groq LLM)
↓
Final Answer
↓
Analytics Storage
(Top Questions + History)

````

---

## ✨ Features

### 🧠 AI Intelligence Layer
- Hybrid RAG (ChromaDB + Semantic Search)
- Llama 3.1 (Groq) response generation
- Context-aware answering system
- Web search fallback for unknown queries

---

### 🔧 Tool-Augmented System
- 📅 Date Tool → handles time/date queries  
- 🧮 Calculator Tool → solves mathematical expressions  
- 🌐 Web Search Tool → DuckDuckGo integration  
- 🔀 Query Router → automatically selects Tool vs RAG  

---

### 📊 Analytics System
- 🔥 Top frequently asked questions
- 🕘 Recent session-based history
- 💾 Persistent question tracking

---

### 🧪 Evaluation System
- RAGAS-based evaluation framework  
- Metrics:
  - Faithfulness
  - Answer Relevancy
  - Context Precision

---

## 🏗️ System Architecture

```mermaid
flowchart TD

A[User Query] --> B[Streamlit UI]

B --> C{Query Router}

C -->|Date| D[Date Tool]
C -->|Calculator| E[Calculator Tool]
C -->|Web Search| F[DuckDuckGo Tool]
C -->|Placement Query| G[RAG Pipeline]

G --> H[ChromaDB Retriever]
H --> I[Context Formation]
I --> J[Groq Llama 3.1 LLM]
J --> K[Final Answer]

D --> K
E --> K
F --> K
````

---

## ⚙️ Tech Stack

| Layer      | Technology           |
| ---------- | -------------------- |
| Frontend   | Streamlit            |
| LLM        | Groq (Llama 3.1)     |
| Vector DB  | ChromaDB             |
| Embeddings | SentenceTransformers |
| Retrieval  | Semantic Search      |
| Tools      | Custom Python Tools  |
| Web Search | DuckDuckGo           |
| Evaluation | RAGAS                |
| Language   | Python               |

---

## 📁 Project Structure

```text
src/
├── rag/
│   ├── retriever.py
│   └── chain.py
│
├── tools/
│   ├── router.py
│   ├── date_tool.py
│   ├── calculator.py
│   ├── web_search.py
│   └── mysql_tool.py
│
├── services/
│   ├── qa_service.py
│   ├── analytics_service.py
│   └── session_service.py
│
├── evaluation/
│   └── ragas_evaluator.py
│
app.py
requirements.txt
README.md
```

---

## 🚀 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/placement-rag-assistant.git
cd placement-rag-assistant
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment

Create `.env` file:

```text
GROQ_API_KEY=your_api_key
```

---

### 5️⃣ Run Application

```bash
streamlit run app.py
```

---

## 💬 Sample Queries

* What is Amazon’s CGPA cutoff?
* CEO of Microsoft
* List top paying companies
* Interview pattern for Google
* What is today's date?
* Current tech trends in 2026

---

## 📊 RAGAS Evaluation

| Metric            | Description                   |
| ----------------- | ----------------------------- |
| Faithfulness      | Accuracy of answer vs context |
| Answer Relevancy  | Relevance of response         |
| Context Precision | Quality of retrieved context  |

---

## 🔥 Key Highlights

* ⚡ Hybrid RAG architecture (Semantic + Tool Routing)
* 🧠 Grounded LLM responses (reduced hallucination)
* 🌐 Web fallback for unknown queries
* 📊 Analytics dashboard (Top + Recent questions)
* 🧪 RAGAS evaluation integration
* 🔧 Modular production-ready architecture

---

## 🧩 Challenges Solved

* Intelligent query routing (Tool vs RAG)
* Handling unknown queries safely
* Improving retrieval accuracy with ChromaDB
* Preventing hallucinated answers
* Building analytics tracking system

---

## 🔮 Future Improvements

* Voice-based assistant
* Multi-college dataset support
* Real-time placement updates
* Cloud deployment (AWS / Render)
* Advanced analytics dashboard with graphs
* Chat memory for multi-turn reasoning

---

## 👩‍💻 Author

**Srisilpa**
BTech IT Student | AI & RAG Systems Developer

---

## 📜 License

This project is licensed under the MIT License.


