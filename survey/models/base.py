from datetime import datetime, timezone

from survey.extensions import db


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(
        db.DateTime, default=lambda: datetime.now(timezone.utc)
    )
    updated_at = db.Column(db.DateTime, nullable=True)

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
        else:
            db.session.flush()
        return self

    def update(self, commit=True):
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        if commit:
            db.session.commit()
        else:
            db.session.flush()

    def __eq__(self, other):
        if not isinstance(other, Base):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.id == other.id
