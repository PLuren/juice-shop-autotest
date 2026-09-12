import requests

from common.logger import get_logger
from settings import base_url

logger = get_logger(__name__)


class RequestClient:
    def __init__(self):
        self.base_url = base_url.rstrip("/")
        self.timeout = 5
        self.session = requests.Session()

    def request(self, method, path, **kwargs):
        url = f"{self.base_url}{path}"
        kwargs.setdefault("timeout", self.timeout)

        logger.info("%s %s", method.upper(), url)
        response = self.session.request(method, url, **kwargs)
        logger.info("%s %s -> %s", method.upper(), url, response.status_code)

        return response

    def get(self, path, **kwargs):
        return self.request("GET", path, **kwargs)

    def post(self, path, **kwargs):
        return self.request("POST", path, **kwargs)

    def put(self, path, **kwargs):
        return self.request("PUT", path, **kwargs)

    def delete(self, path, **kwargs):
        return self.request("DELETE", path, **kwargs)