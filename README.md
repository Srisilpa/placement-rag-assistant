🎯 Placement Intelligence Assistant

An AI-powered Placement Intelligence System that enables students to query placement-related data using natural language.
Built using Hybrid RAG (ChromaDB + Semantic Search), Tool-Augmented Reasoning, Analytics Tracking, and RAGAS Evaluation.

🚀 Features
🧠 Core AI System
Hybrid RAG pipeline (ChromaDB + semantic retrieval)
Llama 3.1 (Groq) powered response generation
Context-aware answering system
Web search fallback for unknown queries
🔧 Tool-Augmented Intelligence
📅 Date Tool → handles time/date queries
🧮 Calculator Tool → solves mathematical expressions
🌐 Web Search Tool → DuckDuckGo integration
🔀 Query Router → automatically selects tool vs RAG
📊 Analytics System
🔥 Top frequently asked questions
🕘 Recent question history (session-based)
💾 Question logging (MySQL / storage layer)
🧪 Evaluation System
RAGAS-based evaluation pipeline
Metrics:
Faithfulness
Answer Relevancy
Context Precision
🧠 System Architecture
User Query
   ↓
Query Router (tool detection)
   ↓
 ┌───────────────┬───────────────┬───────────────┐
 │ Date Tool     │ Calculator    │ Web Search    │
 └───────────────┴───────────────┴───────────────┘
           ↓
        RAG Pipeline
           ↓
   Retriever (ChromaDB)
           ↓
   Context Formation
           ↓
   LLM (Llama 3.1 - Groq)
           ↓
      Final Answer
📁 Project Structure
src/
│
├── rag/
│   ├── retriever.py        # ChromaDB retrieval logic
│   └── chain.py            # LLM response generation
│
├── tools/
│   ├── router.py           # Query classification logic
│   ├── date_tool.py
│   ├── calculator.py
│   ├── web_search.py
│   └── mysql_tool.py       # Logging system
│
├── services/
│   ├── qa_service.py       # Main RAG + tool orchestration
│   ├── analytics_service.py# Top/recent question tracking
│   └── session_service.py # Chat history handling
│
├── evaluation/
│   └── ragas_evaluator.py # RAGAS evaluation pipeline
│
app.py                      # Streamlit UI
requirements.txt
README.md
⚙️ Tech Stack
Layer	Technology
Frontend	Streamlit
LLM	Groq (Llama 3.1)
Vector DB	ChromaDB
Embeddings	SentenceTransformers
Tooling	Custom Python Tools
Search	DuckDuckGo
Evaluation	RAGAS
Language	Python
🚀 How to Run
1️⃣ Clone Repository
git clone https://github.com/Srisilpa/placement-rag-assistant.git
cd placement-rag-assistant
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Setup Environment Variables

Create .env file:

GROQ_API_KEY=your_api_key
5️⃣ Run Application
streamlit run app.py
💬 Example Queries
What is Amazon’s CGPA cutoff?
CEO of Microsoft
List top paying companies
Interview pattern for Google
What is today's date?
Current tech trends in 2026
📊 RAGAS Evaluation
Metric	Description
Faithfulness	How accurate answer is to context
Answer Relevancy	How relevant response is to query
Context Precision	Quality of retrieved context
🔥 Key Highlights
⚡ Hybrid RAG architecture (semantic + tool routing)
🧠 LLM-based grounded response generation
🌐 Web fallback system for unknown queries
📊 Real-time analytics dashboard
🧪 RAGAS evaluation integration
🔧 Modular clean architecture (production-style)
🚀 Future Improvements
Voice-based assistant
Multi-college dataset support
Advanced agentic reasoning
Real-time placement updates
Cloud deployment (Render/AWS)
Advanced analytics dashboard with graphs
👩‍💻 Author

Srisilpa
BTech IT Student | AI & RAG Systems Developer

📜 License

This project is licensed under the MIT License.

💎 Why THIS README is better for YOUR repo

✔ Matches your real folder structure
✔ Explains src/services/tools/evaluation properly
✔ Shows system depth (important for placements)
✔ Clean + professional + recruiter-friendly
✔ No fake or overhyped features
✔ Looks like a real production AI system