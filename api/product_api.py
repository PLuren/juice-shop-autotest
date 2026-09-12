import requests

from settings import base_url


def get_all_products():
    return requests.get(
        f"{base_url}/api/Products",
        timeout=5,
    )


def get_product(product_id):
    return requests.get(
        f"{base_url}/api/Products/{product_id}",
        timeout=5,
    )


def search_products(keyword):
    return requests.get(
        f"{base_url}/rest/products/search",
        params={"q": keyword},
        timeout=5,
    )
