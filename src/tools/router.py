def route_query(query: str):
    if any(x in query.lower() for x in ["date", "today"]):
        return "date"
    if "/" in query:
        return "calculator"
    return "rag"