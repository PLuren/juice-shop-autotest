import requests

from settings import base_url
from common.request_client import RequestClient
client = RequestClient()
def get_cart(bid, headers):
    return client.get(
        f"/rest/basket/{bid}",
        headers=headers,
        timeout=5,
    )


def add_item(bid, product_id, headers, quantity=1):
    return client.post(
        "/api/BasketItems",
        headers=headers,
        json={
            "ProductId": product_id,
            "BasketId": bid,
            "quantity": quantity,
        },
        timeout=5,
    )


def update_item(basket_item_id, quantity, headers):
    return client.put(
        f"/api/BasketItems/{basket_item_id}",
        headers=headers,
        json={"quantity": quantity},
        timeout=5,
    )


def delete_item(basket_item_id, headers):
    return client.delete(
        f"/api/BasketItems/{basket_item_id}",
        headers=headers,
        timeout=5,
    )
