from api.product_api import get_all_products, get_product, search_products
from data.product_cases import (
    PRODUCT_ID,
    PRODUCT_NAME,
    PRODUCT_PRICE,
    PRODUCT_SEARCH_KEYWORD,
)
from common.assertions import assert_status_code,assert_json_value,get_json_value


def test_get_all_products():
    resp = get_all_products()
    assert_status_code(resp,200)
    products = get_json_value(resp,["data"])
    assert isinstance(products, list)
    assert len(products) > 0


def test_get_single_product():
    resp = get_product(PRODUCT_ID)
    assert_status_code(resp,200)

    assert_json_value(resp,["data","id"],PRODUCT_ID)
    assert_json_value(resp,["data","name"],PRODUCT_NAME)
    assert_json_value(resp,["data","price"],PRODUCT_PRICE)



def test_search_products():
    resp = search_products(PRODUCT_SEARCH_KEYWORD)
    assert_status_code(resp,200)
    names = [product["name"].lower() for product in resp.json()["data"]]
    assert any(PRODUCT_SEARCH_KEYWORD in name for name in names)
