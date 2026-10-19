import pytest

import config


@pytest.mark.smoke
@pytest.mark.regression
def test_valid_login_and_logout(login_page):
    inventory = login_page.login(config.STANDARD_USER, config.PASSWORD)
    assert inventory.is_loaded()

    login_after_logout = inventory.logout()
    assert login_after_logout.is_present(login_after_logout.LOGIN_BUTTON)


@pytest.mark.regression
def test_locked_out_user_sees_error(login_page):
    message = login_page.login_expecting_error(config.LOCKED_OUT_USER, config.PASSWORD)
    assert "locked out" in message.lower()


@pytest.mark.regression
def test_wrong_password_shows_error(login_page):
    message = login_page.login_expecting_error(config.STANDARD_USER, "not_the_password")
    assert "do not match any user" in message.lower()


@pytest.mark.regression
def test_empty_username_shows_error(login_page):
    message = login_page.login_expecting_error("", config.PASSWORD)
    assert "username is required" in message.lower()


@pytest.mark.regression
def test_empty_password_shows_error(login_page):
    message = login_page.login_expecting_error(config.STANDARD_USER, "")
    assert "password is required" in message.lower()
