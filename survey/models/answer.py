import bcrypt

from survey.extensions import db

from .base import Base


class Answer(Base):
    """Answer docstring"""

    __tablename__ = "answer"

    survey_id = db.Column(db.Integer, db.ForeignKey("survey.id"))
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    option_id = db.Column(db.Integer, db.ForeignKey("option.id"))
