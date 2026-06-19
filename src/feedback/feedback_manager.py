from src.database.feedback_repository import (
    FeedbackRepository
)


class FeedbackManager:

    def __init__(self):

        self.repo = FeedbackRepository()

    def save(
        self,
        question,
        answer,
        feedback
    ):

        self.repo.save_feedback(
            question,
            answer,
            feedback
        )