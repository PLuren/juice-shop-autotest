import requests
from common.request_client import RequestClient
#from settings import base_url被上面那条取代了

client = RequestClient()
def login(email, password):
    return client.post(
        "/rest/user/login",
        json={"email": email, "password": password},
    )
