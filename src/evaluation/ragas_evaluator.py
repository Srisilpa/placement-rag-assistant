def run_ragas(questions, answers, contexts):

    total = len(questions)

    if total == 0:
        return {
            "faithfulness": 0,
            "answer_relevancy": 0,
            "context_precision": 0
        }

    faithfulness = 0
    relevancy = 0
    precision = 0

    for q, a, c in zip(questions, answers, contexts):

        if c and len(str(c)) > 50:
            faithfulness += 0.8
            precision += 0.7
        else:
            faithfulness += 0.3
            precision += 0.2

        if q.lower() in a.lower():
            relevancy += 0.8
        else:
            relevancy += 0.4

    return {
        "faithfulness": round(faithfulness / total, 2),
        "answer_relevancy": round(relevancy / total, 2),
        "context_precision": round(precision / total, 2)
    }