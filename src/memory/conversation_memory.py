class ConversationMemory:

    def get_recent_context(
        self,
        chat_history,
        limit=3
    ):

        if not chat_history:
            return ""

        history = chat_history[-limit:]

        context = ""

        for item in history:

            context += (
                f"User: {item['question']}\n"
                f"Assistant: {item['answer']}\n"
            )

        return context