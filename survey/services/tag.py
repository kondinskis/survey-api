from datetime import datetime, timezone
from werkzeug.exceptions import NotFound, BadRequest
from survey.extensions import db
from survey.models.tag import Tag


class TagService:
    @staticmethod
    def create(tag):
        new_tag = Tag(
            title=tag.get("title"),
            description=tag.get("description", ""),
        )

        return new_tag.save()

    @staticmethod
    def update(id, tag):
        saved_tag = Tag.query.get(id)
        if saved_tag is None:
            raise NotFound(description=("Tag with id [{0}] not found".format(id)))

        saved_tag.title = tag.get("title")
        saved_tag.description = tag.get("description")
        saved_tag.updated_at = datetime.now(timezone.utc)

        return saved_tag.update()

    @staticmethod
    def delete(id):
        tag = Tag.query.get(id)
        if tag is None:
            raise NotFound(description=("Tag with id [{0}] not found".format(id)))
        return tag.delete()

    @staticmethod
    def get(id):
        tag = Tag.query.get(id)
        if tag is None:
            raise NotFound(description=("Tag with id [{0}] not found".format(id)))
        return tag

    @staticmethod
    def get_all():
        return Tag.query.all()
