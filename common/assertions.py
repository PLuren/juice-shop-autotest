# def assert_status_code(response, expected_status):
#     assert response.status_code == expected_status, (
#         f"状态码错误: expected={expected_status}, actual={response.status_code}, "
#         f"url={response.url}, body={response.text[:200]}"
#     )
#
#
# def get_json_value(response, path):
#     value = response.json()
#     for key in path:
#         value = value[key]
#     return value
#
#
# def assert_json_value(response, path, expected_value):
#     actual_value = get_json_value(response, path)
#     assert actual_value == expected_value, (
#         f"JSON 字段错误: path={path}, expected={expected_value}, actual={actual_value}"
#     )
import json
from datetime import datetime
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)


def save_failure_response(response, prefix):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")

    try:
        body = response.json()
    except ValueError:
        body = response.text

    content = {
        "url": response.url,
        "status_code": response.status_code,
        "body": body,
    }

    path = LOG_DIR / f"{prefix}_{timestamp}.json"

    with path.open("w", encoding="utf-8") as file:
        json.dump(content, file, ensure_ascii=False, indent=2)

    return path


def assert_status_code(response, expected_status):
    if response.status_code != expected_status:
        path = save_failure_response(response, "status_failure")
        raise AssertionError(
            f"状态码错误: expected={expected_status}, "
            f"actual={response.status_code}, "
            f"url={response.url}, saved={path}"
        )


def get_json_value(response, path):
    value = response.json()
    for key in path:
        value = value[key]
    return value


def assert_json_value(response, path, expected_value):
    actual_value = get_json_value(response, path)

    if actual_value != expected_value:
        file_path = save_failure_response(response, "json_failure")
        raise AssertionError(
            f"JSON 字段错误: path={path}, "
            f"expected={expected_value}, "
            f"actual={actual_value}, "
            f"saved={file_path}"
        )