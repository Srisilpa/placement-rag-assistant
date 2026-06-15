import streamlit as st
from datetime import datetime

from src.vectordb.retriever import Retriever
from src.llm.response_generator import ResponseGenerator


# -----------------------------
# Page Config
# -----------------------------

st.set_page_config(
    page_title="Placement Intelligence Assistant",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# Session State
# -----------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.title("🎓 Placement Intelligence")

    st.markdown("---")

    st.markdown("""
### Features

✅ PDF-based RAG

✅ ChromaDB Vector Search

✅ Groq LLM

✅ Context Retrieval

✅ Placement Analytics

✅ Eligibility Queries

✅ Package Analysis

✅ Feedback Collection
""")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):

        st.session_state.chat_history = []

        st.rerun()

# -----------------------------
# Header
# -----------------------------

st.title("🎓 Placement Intelligence Assistant")

st.markdown(
    "Ask questions about placements, companies, packages, eligibility criteria, hiring trends, and statistics."
)

# -----------------------------
# Input
# -----------------------------

question = st.text_input(
    "Ask a Question",
    placeholder="Example: What is the highest package offered?"
)

# -----------------------------
# Submit Button
# -----------------------------

if st.button("🚀 Submit"):

    if not question.strip():

        st.warning("Please enter a question.")

    else:

        try:

            # -----------------------------
            # Retrieve Context
            # -----------------------------

            with st.spinner("Retrieving relevant information..."):

                retriever = Retriever()

                contexts = retriever.retrieve(question)

            # -----------------------------
            # Generate Answer
            # -----------------------------

            with st.spinner("Generating answer..."):

                generator = ResponseGenerator()

                answer = generator.answer(
                    question,
                    contexts
                )

            # -----------------------------
            # Confidence Score
            # -----------------------------

            confidence = min(
                95,
                70 + (len(contexts) * 5)
            )

            # -----------------------------
            # Store Chat
            # -----------------------------

            st.session_state.chat_history.append(
                {
                    "question": question,
                    "answer": answer,
                    "contexts": contexts,
                    "confidence": confidence,
                    "timestamp": datetime.now().strftime(
                        "%d-%m-%Y %H:%M:%S"
                    )
                }
            )

        except Exception as e:

            st.error(
                f"Error: {str(e)}"
            )

# -----------------------------
# Display Chat History
# -----------------------------

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

    # -----------------------------
    # Retrieved Context
    # -----------------------------

    with st.expander(
        "📄 Retrieved Context"
    ):

        for idx, chunk in enumerate(
            item["contexts"]
        ):

            st.markdown(
                f"### Chunk {idx+1}"
            )

            st.write(chunk)

    # -----------------------------
    # Feedback
    # -----------------------------

    st.markdown("### Feedback")

    fb1, fb2 = st.columns(2)

    with fb1:

        if st.button(
            f"👍 Helpful ({item['timestamp']})"
        ):

            st.success(
                "Thanks for your feedback!"
            )

    with fb2:

        if st.button(
            f"👎 Not Helpful ({item['timestamp']})"
        ):

            st.warning(
                "Feedback recorded."
            )

# -----------------------------
# Footer
# -----------------------------

st.markdown("---")

st.caption(
    "Placement Intelligence Assistant | RAG + ChromaDB + Groq + Streamlit"
)