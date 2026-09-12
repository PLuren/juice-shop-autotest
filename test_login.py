import pytest

from api.login_api import login
# from data.login_cases import LOGIN_CASES改良成下两条
from data.loader import load_json
LOGIN_CASES = load_json("login_cases.json")
from settings import email,password
from common.assertions import assert_json_value,assert_status_code,get_json_value

def test_login_success():
    resp = login(email, password)
    assert_status_code(resp,200)
    token = get_json_value(resp,["authentication","token"])
    assert token.startswith("eyJ")



@pytest.mark.parametrize("case",LOGIN_CASES)
def test_login_parametrized(case):
    resp = login(case["email"], case["password"])
    assert_status_code(resp,case["expected_status"])
