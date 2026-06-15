from datetime import datetime

from sqlalchemy.orm import Session

from src.database.mysql_connection import engine
from src.database.models import Feedback


class FeedbackRepository:

    def save_feedback(
        self,
        question,
        answer,
        feedback
    ):

        session = Session(engine)

        record = Feedback(
            question=question,
            answer=answer,
            feedback=feedback,
            created_at=datetime.now()
        )

        session.add(record)

        session.commit()

        session.close()