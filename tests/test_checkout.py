import pytest


def _start_checkout(inventory_page, items=2):
    inventory_page.add_first_items(items)
    return inventory_page.open_cart().checkout()


@pytest.mark.smoke
@pytest.mark.regression
def test_complete_two_item_checkout(inventory_page):
    names = inventory_page.item_names()
    checkout = _start_checkout(inventory_page, items=2)

    checkout.fill_info("Chris", "Magill", "37201")
    checkout.continue_to_overview()
    assert sorted(checkout.overview_item_names()) == sorted(names[:2])

    checkout.finish()
    assert "thank you for your order" in checkout.confirmation_text().lower()


@pytest.mark.regression
def test_missing_first_name_shows_error(inventory_page):
    checkout = _start_checkout(inventory_page, items=1)
    checkout.fill_info("", "Magill", "37201")
    checkout.continue_to_overview()
    assert "first name is required" in checkout.error_message().lower()


@pytest.mark.regression
def test_missing_postal_code_shows_error(inventory_page):
    checkout = _start_checkout(inventory_page, items=1)
    checkout.fill_info("Chris", "Magill", "")
    checkout.continue_to_overview()
    assert "postal code is required" in checkout.error_message().lower()


@pytest.mark.regression
def test_reset_app_state_clears_cart(inventory_page):
    inventory_page.add_first_items(2)
    assert inventory_page.cart_count() == 2

    inventory_page.reset_app_state()
    assert inventory_page.cart_count() == 0
