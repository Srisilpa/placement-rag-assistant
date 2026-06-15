import sys
from pathlib import Path

project_root = Path(__file__).parent.parent

sys.path.append(
    str(project_root)
)

from src.memory.conversation_memory import (
    ConversationMemory
)

memory = ConversationMemory()

history = [
    {
        "question": "Amazon package?",
        "answer": "28.6 LPA"
    },
    {
        "question": "Google package?",
        "answer": "42.0 LPA"
    }
]

print(
    memory.get_recent_context(
        history
    )
)