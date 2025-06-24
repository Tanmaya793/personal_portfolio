from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class Contact(FlaskForm):

    firstname = StringField(
        "First Name",
        validators = [DataRequired(), Length(2,14)]
    )

    lastname = StringField(
        "Last Name",
        validators = [DataRequired(), Length(2,14)]
    )

    email = StringField(
        "Email",
        validators = [DataRequired(), Email()]
    )

    message = TextAreaField(
        "Message/Feedback"
    )

    submit = SubmitField(
        "Submit"
    )