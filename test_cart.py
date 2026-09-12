from api.cart_api import add_item, delete_item, get_cart, update_item
from api.product_api import get_all_products
from data.cart_cases import CART_ITEM_QUANTITY


def test_cart_crud_flow(login_info):
    headers = login_info["headers"]
    bid = login_info["bid"]

    cart = get_cart(bid, headers)
    assert cart.status_code == 200
    existing_ids = {product["id"] for product in cart.json()["data"]["Products"]}

    products = get_all_products().json()["data"]
    product_id = next(
        product["id"] for product in products if product["id"] not in existing_ids
    )

    added = add_item(bid, product_id, headers)
    assert added.status_code == 200
    basket_item_id = added.json()["data"]["id"]

    updated = update_item(basket_item_id, CART_ITEM_QUANTITY, headers)
    assert updated.status_code == 200
    assert updated.json()["data"]["quantity"] == CART_ITEM_QUANTITY

    verified = get_cart(bid, headers)
    items = verified.json()["data"]["Products"]
    assert any(
        item["BasketItem"]["id"] == basket_item_id
        and item["BasketItem"]["quantity"] == CART_ITEM_QUANTITY
        for item in items
    )

    deleted = delete_item(basket_item_id, headers)
    assert deleted.status_code == 200

    final_cart = get_cart(bid, headers)
    remaining_ids = [
        item["BasketItem"]["id"]
        for item in final_cart.json()["data"]["Products"]
    ]
    assert basket_item_id not in remaining_ids
