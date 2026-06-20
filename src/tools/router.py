import re

def route_query(query: str):

    q = query.lower().strip()

    # ---------------- DATE ----------------
    if any(x in q for x in ["date", "today", "time"]):
        return "date"

    # ---------------- CALCULATOR ----------------
    if re.search(r"\d+\s*[\+\-\*/%]\s*\d+", q):
        return "calculator"

    # ---------------- STRONG WEB INTENT ----------------
    web_force = [
        "ceo", "who is", "what is", "president",
        "founder", "head of", "owner",
        "latest", "current", "news",
        "salary", "trend", "update",
        "google", "microsoft", "amazon"
    ]

    # MUST GO WEB
    if any(w in q for w in web_force):
        return "web"

    # ANY QUESTION → WEB (CRITICAL FIX)
    if q.startswith(("who", "what", "when", "which")):
        return "web"

    return "rag"