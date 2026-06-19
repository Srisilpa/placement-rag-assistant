from src.rag.retriever import retrieve_docs
from src.rag.chain import generate_answer

from src.tools.mysql_tool import save_question
from src.services.analytics_service import save_question_stat


def answer_question(
    question,
    session_id
):

    docs = retrieve_docs(question)

    print("=" * 50)
    print("Retrieved Docs:", len(docs))
    print("=" * 50)

    context = "\n\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )

    if not context.strip():

        answer = (
            "I couldn't find relevant "
            "information in the dataset."
        )

    else:

        answer = generate_answer(
            context=context,
            question=question
        )

    save_question(
        session_id,
        question,
        answer
    )

    save_question_stat(question)

    return answer, context