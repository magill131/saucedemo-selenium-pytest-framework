import pytest


@pytest.mark.regression
def test_sort_price_low_to_high(inventory_page):
    inventory_page.sort_by("Price (low to high)")
    prices = inventory_page.item_prices()
    assert prices == sorted(prices)


@pytest.mark.regression
def test_sort_name_a_to_z(inventory_page):
    inventory_page.sort_by("Name (Z to A)")
    inventory_page.sort_by("Name (A to Z)")
    names = inventory_page.item_names()
    assert names == sorted(names)


@pytest.mark.smoke
@pytest.mark.regression
def test_add_item_updates_cart_badge(inventory_page):
    assert inventory_page.cart_count() == 0
    inventory_page.add_item(0)
    assert inventory_page.cart_count() == 1


@pytest.mark.regression
def test_add_multiple_items_updates_cart_badge(inventory_page):
    inventory_page.add_first_items(3)
    assert inventory_page.cart_count() == 3


@pytest.mark.regression
def test_remove_item_clears_cart_badge(inventory_page):
    inventory_page.add_item(0)
    inventory_page.remove_item(0)
    assert inventory_page.cart_count() == 0
