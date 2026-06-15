import json
import os


class QuestionTracker:

    def __init__(
        self,
        file_path="data/question_stats.json"
    ):

        self.file_path = file_path

        if not os.path.exists(
            self.file_path
        ):

            with open(
                self.file_path,
                "w"
            ) as f:

                json.dump(
                    {},
                    f
                )

    def add_question(
        self,
        question
    ):

        data = self.load()

        data[question] = (
            data.get(
                question,
                0
            )
            + 1
        )

        with open(
            self.file_path,
            "w"
        ) as f:

            json.dump(
                data,
                f,
                indent=4
            )

    def load(self):

        with open(
            self.file_path,
            "r"
        ) as f:

            return json.load(
                f
            )

    def get_top_questions(
        self,
        limit=5
    ):

        data = self.load()

        return sorted(
            data.items(),
            key=lambda x: x[1],
            reverse=True
        )[:limit]