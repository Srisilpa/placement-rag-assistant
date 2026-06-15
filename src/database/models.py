from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Feedback(Base):

    __tablename__ = "feedback"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    question = Column(
        String(2000)
    )

    answer = Column(
        String(10000)
    )

    feedback = Column(
        String(20)
    )

    created_at = Column(
        DateTime
    )