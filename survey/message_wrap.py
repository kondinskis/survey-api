from flask_mail import Message
from jinja2 import Template
from flask import current_app


class MessageWrap(Message):
    def __init__(self, subject, recipients, template, data):
        super().__init__(subject=subject, recipients=recipients)
        data["base_url"] = current_app.config["MAIL_BASE_URL"]
        self.html = self._load_template(template, data)

    def _load_template(self, template, data):
        with open("survey/templates/%s.html" % template, "r") as t_file:
            return Template(t_file.read()).render(data)
