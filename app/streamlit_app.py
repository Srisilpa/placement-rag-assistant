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
    clear_session_history,
    get_total_questions
)
from src.services.session_service import get_history


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Placement Intelligence System",
    layout="wide"
)


# --------------------------------------------------
# SESSION INIT
# --------------------------------------------------
if "session_id" not in st.session_state:
    st.session_state.session_id = (
        str(uuid.uuid4())
        .replace("-", "")[:16]
    )

if "selected_question" not in st.session_state:
    st.session_state.selected_question = None

if "last_context" not in st.session_state:
    st.session_state.last_context = ""

session_id = st.session_state.session_id


# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.title("🎯 Placement Intelligence System")
st.caption(
    "Ask placement-related questions from your dataset"
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.title("📊 Dashboard")

st.sidebar.subheader("📁 Project Details")

st.sidebar.info(
    f"""
Dataset : Placement_RAG_Dataset_Enhanced

Vector DB : Chroma

Retriever : Semantic Search

LLM : Llama 3.1

Questions Asked :
{get_total_questions()}
"""
)

# --------------------------------------------------
# CLEAR CHAT
# --------------------------------------------------
if st.sidebar.button("🧹 Clear Chat"):

    clear_session_history(session_id)

    st.session_state.selected_question = None
    st.session_state.last_context = ""

    st.rerun()


# --------------------------------------------------
# TOP QUESTIONS
# --------------------------------------------------
st.sidebar.subheader("🔥 Top 5 Questions")

try:

    top_questions = get_top_questions(limit=5)

    if top_questions:

        for q in top_questions:

            question = q.get(
                "question",
                "Unknown Question"
            )

            count = q.get(
                "count",
                0
            )

            st.sidebar.write(
                f"**{count}x** - {question}"
            )

    else:

        st.sidebar.info(
            "No questions asked yet."
        )

except Exception as e:

    st.sidebar.error(
        f"Top Questions Error: {e}"
    )


# --------------------------------------------------
# RECENT QUESTIONS
# --------------------------------------------------
st.sidebar.subheader("🕘 Recent Questions")

try:

    recent_questions = get_recent_questions(
    session_id
) 

    if recent_questions:

        for i, q in enumerate(recent_questions):

            question = q.get(
                "question",
                "Unknown Question"
            )

            answer = q.get(
                "answer",
                "No answer available"
            )

            with st.sidebar.expander(
                question[:60]
            ):

                st.write(answer)

                if st.button(
                    "Ask Again",
                    key=f"recent_{i}"
                ):
                    st.session_state.selected_question = question
                    st.rerun()

    else:

        st.sidebar.info(
            "No recent questions."
        )

except Exception as e:

    st.sidebar.error(
        f"Recent Questions Error: {e}"
    )


# --------------------------------------------------
# CHAT HISTORY
# --------------------------------------------------
try:

    history = get_history(session_id)

    for msg in history:

        question = msg.get(
            "question",
            ""
        )

        answer = msg.get(
            "answer",
            ""
        )

        with st.chat_message("user"):
            st.write(question)

        with st.chat_message("assistant"):
            st.write(answer)

except Exception as e:

    st.error(
        f"History Error: {e}"
    )


# --------------------------------------------------
# CHAT INPUT
# --------------------------------------------------
query = st.chat_input(
    "Ask placement-related questions..."
)

final_query = (
    st.session_state.selected_question
    if st.session_state.selected_question
    else query
)


# --------------------------------------------------
# QUESTION PROCESSING
# --------------------------------------------------
if final_query:

    with st.chat_message("user"):
        st.write(final_query)

    try:

        with st.spinner(
            "🔍 Searching documents..."
        ):

            answer, context = answer_question(
                final_query,
                session_id
            )

        st.session_state.last_context = context

        with st.chat_message("assistant"):
            st.write(answer)

        if context:

            with st.expander(
                "📄 Retrieved Context"
            ):
                st.text(
                    context[:3000]
                )

        st.session_state.selected_question = None

        st.rerun()

    except Exception as e:

        st.error(
            f"Error generating answer: {e}"
        )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")
st.caption(
    "Placement Intelligence Assistant | RAG + Chroma + Streamlit"
)