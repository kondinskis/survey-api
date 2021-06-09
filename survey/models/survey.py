import bcrypt

from survey.extensions import db

from .base import Base

tags = db.Table(
    "tags",
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True),
    db.Column("survey_id", db.Integer, db.ForeignKey("survey.id"), primary_key=True),
)


class Survey(Base):
    __tablename__ = "survey"

    title = db.Column(db.String(length=64))
    description = db.Column(db.String(length=256))
    active_till = db.Column(db.DateTime())
    active_from = db.Column(db.DateTime())
    questions = db.relationship(
        "Question", backref="survey", cascade="all, delete, delete-orphan"
    )
    tags = db.relationship(
        "Tag", secondary=tags, lazy="subquery", backref=db.backref("surveys", lazy=True)
    )
    published = db.Column(db.Boolean())
    login_required = db.Column(db.Boolean())