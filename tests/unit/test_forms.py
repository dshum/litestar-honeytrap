from app.forms import FeedbackForm


def test_feedback_form(feedback_form: FeedbackForm):
    assert feedback_form.first_name.type == "StringField"
    assert feedback_form.last_name.type == "StringField"
    assert feedback_form.email.type == "EmailField"
    assert feedback_form.phone.type == "StringField"
    assert feedback_form.message.type == "TextAreaField"
    assert feedback_form.is_human.type == "BooleanField"


def test_feedback_form_valid(feedback_form: FeedbackForm):
    assert feedback_form.validate() == True


def test_feedback_form_missing_name(feedback_form: FeedbackForm):
    feedback_form.first_name.data = None
    feedback_form.last_name.data = None
    assert feedback_form.validate() == False


def test_feedback_form_invalid_email(feedback_form: FeedbackForm):
    feedback_form.email.data = "invalid-email"
    assert feedback_form.validate() == False
