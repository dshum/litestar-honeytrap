from typing import Any

import pytest

from app.forms import FeedbackForm


@pytest.fixture
def feedback_form(feedback_form_data: dict[str, Any]):
    return FeedbackForm(data=feedback_form_data)
