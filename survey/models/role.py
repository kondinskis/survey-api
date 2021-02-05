from survey.extensions import db

from .base import Base


class Role(Base):
    __tablename__ = "role"

    name = db.Column(db.String(length=32), nullable=False)
