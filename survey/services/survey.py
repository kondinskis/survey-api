from datetime import datetime, timezone
from werkzeug.exceptions import NotFound, BadRequest
from survey.extensions import db
from survey.models.survey import Survey
from survey.models.question import Question
from survey.models.option import Option
from survey.models.answer import Answer
from survey.models.tag import Tag


class SurveyService:
    @staticmethod
    def create(survey):
        tags = Tag.query.filter(Tag.id.in_(survey.get("tag_ids") or [])).all()
        new_survey = Survey(
            title=survey.get("title"),
            description=survey.get("description"),
            active_till=survey.get("active_till"),
            active_from=survey.get("active_from"),
            tags=tags,
        )

        new_survey = new_survey.save(commit=False)

        for question in survey.get("questions"):
            new_question = Question(
                question=question.get("question"),
                order=question.get("order"),
                survey_id=new_survey.id,
            )

            new_question = new_question.save(commit=False)

            for option in question.get("options"):
                new_option = Option(
                    option=option.get("option"),
                    order=option.get("order"),
                    question_id=new_question.id,
                )

                new_option.save(commit=False)

        db.session.commit()
        return new_survey

    @staticmethod
    def update(id, survey):
        saved_survey = Survey.query.get(id)
        if saved_survey is None:
            raise NotFound(description=("Survey with id [{0}] not found".format(id)))

        saved_survey.title = survey.get("title")
        saved_survey.description = survey.get("description")
        saved_survey.active_till = survey.get("active_till")
        saved_survey.active_from = survey.get("active_from")
        saved_survey.updated_at = datetime.now(timezone.utc)
        saved_survey.questions = list(
            map(
                lambda x: Question(
                    id=x.get("id", None),
                    survey_id=saved_survey.id,
                    question=x.get("question"),
                    order=x.get("order"),
                    updated_at=None
                    if x.get("id") is None
                    else datetime.now(timezone.utc),
                    options=list(
                        map(
                            lambda y: Option(
                                id=y.get("id", None),
                                option=y.get("option"),
                                order=y.get("order"),
                                question_id=x.get("id", None),
                                updated_at=None
                                if y.get("id") is None
                                else datetime.now(timezone.utc),
                            ),
                            x.get("options") or [],
                        )
                    ),
                ),
                survey.get("questions") or [],
            )
        )
        saved_survey.tags = Tag.query.filter(
            Tag.id.in_(survey.get("tag_ids") or [])
        ).all()

        saved_survey = saved_survey.update()
        return saved_survey

    @staticmethod
    def delete(id):
        survey = Survey.query.get(id)
        if survey is None:
            raise NotFound(description=("Survey with id [{0}] not found".format(id)))
        return survey.delete()

    @staticmethod
    def get(id):
        survey = Survey.query.get(id)
        print(survey.questions)
        if survey is None:
            raise NotFound(description=("Survey with id [{0}] not found".format(id)))
        return survey

    @staticmethod
    def get_all():
        return Survey.query.all()
