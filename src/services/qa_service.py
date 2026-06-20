from src.rag.retriever import retrieve_docs
from src.rag.chain import generate_answer

from src.tools.router import route_query
from src.tools.date_tool import get_date
from src.tools.calculator import calculate
from src.tools.web_search import search_web

from src.tools.mysql_tool import save_question
from src.services.analytics_service import save_question_stat


def answer_question(question, session_id):

    q = question.lower().strip()
    route = route_query(question)

    context = ""
    answer = ""

    # ==================================================
    # 📅 DATE TOOL
    # ==================================================
    if route == "date":
        answer = get_date()
        context = "DATE_TOOL"

    # ==================================================
    # 🧮 CALCULATOR TOOL
    # ==================================================
    elif route == "calculator":
        answer = calculate(question)
        context = "CALCULATOR_TOOL"

    # ==================================================
    # 🌐 WEB TOOL
    # ==================================================
    elif route == "web":

        results = search_web(question)

        answer = "\n\n".join(
            f"🔹 {r.get('title','')}\n{r.get('body','')}\n{r.get('href','')}"
            for r in results
        )

        context = "WEB_TOOL"

    # ==================================================
    # 🚨 HARD OVERRIDE (CRITICAL FIX FOR CEO / GK QUESTIONS)
    # ==================================================
    elif any(x in q for x in [
        "ceo", "who is", "what is", "founder",
        "president", "head of", "current", "latest"
    ]):
        results = search_web(question)

        answer = "\n\n".join(
            f"🔹 {r.get('title','')}\n{r.get('body','')}\n{r.get('href','')}"
            for r in results
        )

        context = "WEB_OVERRIDE"

    # ==================================================
    # 📚 RAG TOOL
    # ==================================================
    else:

        docs = retrieve_docs(question)

        # If no docs → fallback to web
        if not docs:
            results = search_web(question)

            answer = "\n\n".join(
                f"🔹 {r.get('title','')}\n{r.get('body','')}\n{r.get('href','')}"
                for r in results
            )

            context = "WEB_FALLBACK"

        else:

            context = "\n\n".join(doc.page_content for doc in docs)

            # If weak context → fallback to web
            if len(context.strip()) < 80:
                results = search_web(question)

                answer = "\n\n".join(
                    f"🔹 {r.get('title','')}\n{r.get('body','')}\n{r.get('href','')}"
                    for r in results
                )

                context = "WEB_WEAK_RAG"

            else:

                answer = generate_answer(
                    context=context,
                    question=question
                )

    # ==================================================
    # 💾 SAVE ONLY ONCE
    # ==================================================
    save_question(session_id, question, answer)
    save_question_stat(question)

    return answer, context