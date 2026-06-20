import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import streamlit as st
import uuid

from src.services.qa_service import answer_question
from src.services.analytics_service import (
    get_top_questions,
    get_recent_questions,
    clear_session_history
)
from src.services.session_service import get_history

from src.evaluation.ragas_evaluator import run_ragas


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Placement Intelligence System",
    layout="wide"
)

st.title("🎯 Placement Intelligence System")
st.caption("Ask placement-related questions from your dataset")


# --------------------------------------------------
# SESSION INIT
# --------------------------------------------------
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4()).replace("-", "")[:16]

if "selected_question" not in st.session_state:
    st.session_state.selected_question = None

if "ragas_data" not in st.session_state:
    st.session_state.ragas_data = {
        "questions": [],
        "answers": [],
        "contexts": []
    }

session_id = st.session_state.session_id


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.title("📊 Dashboard")

st.sidebar.subheader("📁 Project Details")

st.sidebar.info(
    """
Dataset : Placement_RAG_Dataset_Enhanced  
Vector DB : Chroma  
Retriever : Semantic Search  
LLM : Llama 3.1  
"""
)


# --------------------------------------------------
# CLEAR CHAT
# --------------------------------------------------
if st.sidebar.button("🧹 Clear Chat"):

    clear_session_history(session_id)

    st.session_state.selected_question = None
    st.session_state.ragas_data = {
        "questions": [],
        "answers": [],
        "contexts": []
    }

    st.rerun()


# --------------------------------------------------
# TOP QUESTIONS
# --------------------------------------------------
st.sidebar.subheader("🔥 Top 5 Questions")

top_questions = get_top_questions(limit=5)

if top_questions:
    for q in top_questions:
        st.sidebar.write(f"**{q.get('count',0)}x** - {q.get('question')}")
else:
    st.sidebar.info("No questions yet")


# --------------------------------------------------
# RECENT QUESTIONS
# --------------------------------------------------
st.sidebar.subheader("🕘 Recent Questions")

recent_questions = get_recent_questions(session_id)

if recent_questions:
    for i, q in enumerate(recent_questions):
        with st.sidebar.expander(q.get("question","")[:60]):

            st.write(q.get("answer",""))

            if st.button("Ask Again", key=f"recent_{i}"):
                st.session_state.selected_question = q.get("question")
                st.rerun()
else:
    st.sidebar.info("No recent questions")


# --------------------------------------------------
# RAGAS SECTION (SIDEBAR)
# --------------------------------------------------
st.sidebar.subheader("📊 RAGAS Evaluation")

if st.sidebar.button("Run Evaluation"):

    try:
        result = run_ragas(
            st.session_state.ragas_data["questions"],
            st.session_state.ragas_data["answers"],
            st.session_state.ragas_data["contexts"]
        )

        st.sidebar.success("Evaluation Completed")

        st.sidebar.metric("Faithfulness", result["faithfulness"])
        st.sidebar.metric("Relevancy", result["answer_relevancy"])
        st.sidebar.metric("Context Precision", result["context_precision"])

    except Exception as e:
        st.sidebar.error(f"RAGAS Error: {e}")


# --------------------------------------------------
# CHAT HISTORY
# --------------------------------------------------
history = get_history(session_id)

for msg in history:
    with st.chat_message("user"):
        st.write(msg.get("question",""))

    with st.chat_message("assistant"):
        st.write(msg.get("answer",""))


# --------------------------------------------------
# INPUT
# --------------------------------------------------
query = st.chat_input("Ask placement-related questions...")


final_query = (
    st.session_state.selected_question
    if st.session_state.selected_question
    else query
)


# --------------------------------------------------
# PROCESS QUERY
# --------------------------------------------------
if final_query:

    with st.chat_message("user"):
        st.write(final_query)

    try:
        with st.spinner("🔍 Searching documents..."):

            answer, context = answer_question(
                final_query,
                session_id
            )

        with st.chat_message("assistant"):
            st.write(answer)

        # Save for RAGAS
        st.session_state.ragas_data["questions"].append(final_query)
        st.session_state.ragas_data["answers"].append(answer)
        st.session_state.ragas_data["contexts"].append([context])

        # Context viewer
        if context:
            with st.expander("📄 Retrieved Context"):
                st.text(context[:3000])

        st.session_state.selected_question = None

        st.rerun()

    except Exception as e:
        st.error(f"Error generating answer: {e}")


# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")
st.caption("Placement Intelligence Assistant | RAG + Chroma + Streamlit + RAGAS")