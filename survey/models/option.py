import bcrypt

from survey.extensions import db

from .base import Base


class Option(Base):
    __tablename__ = "option"

    option = db.Column(db.String(length=64))
    order = db.Column(db.Integer)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
