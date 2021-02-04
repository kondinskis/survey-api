import bcrypt

from survey.extensions import db

from .base import Base


class Question(Base):
    __tablename__ = "question"

    question = db.Column(db.String(length=128))
    order = db.Column(db.Integer)
    survey_id = db.Column(db.Integer, db.ForeignKey("survey.id"))