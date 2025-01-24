from wtforms.fields.simple import StringField, EmailField, TextAreaField, BooleanField
from wtforms.form import Form
from wtforms.validators import DataRequired, Length, Optional, Email


class FeedbackForm(Form):
    first_name = StringField("First name",
                             validators=[DataRequired(), Length(max=100)],
                             render_kw={"placeholder": "First name"})
    last_name = StringField("Last name",
                            validators=[DataRequired(), Length(max=100)],
                            render_kw={"placeholder": "Last name"})
    email = EmailField("Email",
                       validators=[DataRequired(), Email("Invalid email address")],
                       render_kw={"placeholder": "Email"})
    phone = StringField("Phone",
                        validators=[Optional()],
                        render_kw={"placeholder": "Phone"})
    message = TextAreaField("Message",
                            validators=[DataRequired(), Length(min=10, max=1000)],
                            render_kw={"placeholder": "Please write a message...", "rows": 5})
    is_human = BooleanField("I'm not a robot")
