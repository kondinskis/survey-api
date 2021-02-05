from survey.extensions import db

from .base import Base


class Tag(Base):
    __tablename__ = "tag"

    title = db.Column(db.String(length=64))
    description = db.Column(db.String(length=256))