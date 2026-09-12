import pytest

from api.login_api import login
from settings import email, password


@pytest.fixture()
def login_info():
    resp = login(email, password)
    assert resp.status_code == 200

    auth = resp.json()["authentication"]
    return {
        "token": auth["token"],
        "bid": auth["bid"],
        "headers": {"Authorization": f"Bearer {auth['token']}"},
    }
