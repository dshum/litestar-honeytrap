from typing import Any

import pytest

pytest_plugins = []


@pytest.fixture
def feedback_form_data() -> dict[str, Any]:
    return {
        "first_name": "John",
        "last_name": "Doe",
        "email": "valid-email@example.com",
        "phone": "+5555555555",
        "message": "This is a test message",
        "is_human": True,
    }
