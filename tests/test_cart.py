import pytest


@pytest.mark.regression
def test_cart_lists_added_items(inventory_page):
    names = inventory_page.item_names()
    inventory_page.add_item(0)
    inventory_page.add_item(1)

    cart = inventory_page.open_cart()
    assert cart.is_loaded()
    assert sorted(cart.item_names()) == sorted(names[:2])


@pytest.mark.regression
def test_cart_persists_across_navigation(inventory_page):
    inventory_page.add_item(0)
    cart = inventory_page.open_cart()
    inventory = cart.continue_shopping()

    assert inventory.cart_count() == 1
    assert len(inventory.open_cart().item_names()) == 1


@pytest.mark.regression
def test_remove_item_from_cart(inventory_page):
    inventory_page.add_item(0)
    cart = inventory_page.open_cart()
    cart.remove_item(0)
    assert cart.item_names() == []
