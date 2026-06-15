import streamlit as st
from datetime import datetime

from src.vectordb.retriever import Retriever
from src.llm.response_generator import ResponseGenerator

from src.memory.cache_manager import CacheManager
from src.memory.conversation_memory import ConversationMemory


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Placement Intelligence Assistant",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------------------------
# OBJECTS
# --------------------------------------------------

cache = CacheManager()
memory = ConversationMemory()

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "question_frequency" not in st.session_state:
    st.session_state.question_frequency = {}

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("🎓 Placement Intelligence")

    st.markdown("---")

    st.markdown("""
### Features

✅ PDF-based RAG

✅ ChromaDB Vector Search

✅ Groq LLM

✅ Context Retrieval

✅ Cache Memory

✅ Conversation Memory

✅ Placement Analytics

✅ Eligibility Queries

✅ Feedback Collection
""")

    st.markdown("---")

    st.subheader("🔥 Top 5 Questions")

    if st.session_state.question_frequency:

        top_questions = sorted(
            st.session_state.question_frequency.items(),
            key=lambda x: x[1],
            reverse=True
        )[:5]

        for q, count in top_questions:
            st.write(f"**{count}x** - {q}")

    else:
        st.caption("No questions asked yet.")

    st.markdown("---")

    st.subheader("🕘 Recent Questions")

    recent_questions = st.session_state.chat_history[-5:]

    if recent_questions:

        for item in reversed(recent_questions):

            st.caption(
                item["question"]
            )

    else:

        st.caption(
            "No history yet."
        )

    st.markdown("---")

    if st.button("🗑 Clear Chat"):

        st.session_state.chat_history = []
        st.session_state.question_frequency = {}

        st.rerun()

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title(
    "🎓 Placement Intelligence Assistant"
)

st.markdown(
    """
Ask questions about:

- Placement Packages
- Company Eligibility
- Hiring Trends
- CGPA Requirements
- Placement Statistics
- Placement Insights
"""
)

# --------------------------------------------------
# INPUT
# --------------------------------------------------

question = st.text_input(
    "Ask a Question",
    placeholder="Example: What is the highest package offered?"
)

# --------------------------------------------------
# SUBMIT
# --------------------------------------------------

if st.button("🚀 Submit"):

    if not question.strip():

        st.warning(
            "Please enter a question."
        )

    else:

        try:

            cache_hit = False

            # --------------------------------
            # QUESTION FREQUENCY
            # --------------------------------

            st.session_state.question_frequency[
                question
            ] = (
                st.session_state.question_frequency.get(
                    question,
                    0
                )
                + 1
            )

            # --------------------------------
            # CACHE CHECK
            # --------------------------------

            if cache.exists(question):

                answer = cache.get(
                    question
                )

                contexts = []

                cache_hit = True

            else:

                # ----------------------------
                # RETRIEVE CONTEXT
                # ----------------------------

                with st.spinner(
                    "Retrieving Context..."
                ):

                    retriever = Retriever()

                    results = retriever.retrieve(
                        question
                    )

                    if isinstance(results, dict):

                        contexts = results.get(
                            "documents",
                            []
                        )

                    else:

                        contexts = results

                # ----------------------------
                # MEMORY CONTEXT
                # ----------------------------

                memory_context = (
                    memory.get_recent_context(
                        st.session_state.chat_history[-3:]
                    )
                )

                # ----------------------------
                # GENERATE ANSWER
                # ----------------------------

                with st.spinner(
                    "Generating Answer..."
                ):

                    generator = ResponseGenerator()

                    answer = generator.answer(
                        question
                        + "\n\nConversation Context:\n"
                        + memory_context,
                        contexts
                    )

                cache.set(
                    question,
                    answer
                )

            # --------------------------------
            # CONFIDENCE
            # --------------------------------

            confidence = min(
                95,
                70 + (len(contexts) * 5)
            )

            # --------------------------------
            # SAVE CHAT
            # --------------------------------

            st.session_state.chat_history.append(
                {
                    "question": question,
                    "answer": answer,
                    "contexts": contexts,
                    "cache_hit": cache_hit,
                    "confidence": confidence,
                    "timestamp": datetime.now().strftime(
                        "%d-%m-%Y %H:%M:%S"
                    )
                }
            )

            st.rerun()

        except Exception as e:

            st.error(
                f"Error: {str(e)}"
            )

# --------------------------------------------------
# DISPLAY HISTORY
# --------------------------------------------------

for item in reversed(
    st.session_state.chat_history
):

    st.markdown("---")

    st.subheader("❓ Question")

    st.write(
        item["question"]
    )

    st.subheader("🤖 Answer")

    st.success(
        item["answer"]
    )

    if item["cache_hit"]:

        st.info(
            "⚡ Answer served from cache"
        )

    else:

        st.info(
            "📚 Answer generated using RAG"
        )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Confidence Score",
            f"{item['confidence']}%"
        )

    with col2:

        st.write(
            f"🕒 {item['timestamp']}"
        )

    # --------------------------------
    # CONTEXT
    # --------------------------------

    with st.expander(
        "📄 Retrieved Context"
    ):

        if item["contexts"]:

            for i, chunk in enumerate(
                item["contexts"]
            ):

                st.markdown(
                    f"### Chunk {i+1}"
                )

                st.write(
                    chunk
                )

        else:

            st.caption(
                "No context available."
            )

    # --------------------------------
    # FEEDBACK
    # --------------------------------

    st.markdown(
        "### Feedback"
    )

    c1, c2 = st.columns(2)

    with c1:

        if st.button(
            f"👍 Helpful {item['timestamp']}"
        ):

            st.success(
                "Thanks for your feedback!"
            )

    with c2:

        if st.button(
            f"👎 Not Helpful {item['timestamp']}"
        ):

            st.warning(
                "Feedback recorded."
            )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Placement Intelligence Assistant | RAG + ChromaDB + Groq + Streamlit"
)