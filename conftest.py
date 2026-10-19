import os
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import config
from pages.login_page import LoginPage

SCREENSHOT_DIR = Path("reports") / "screenshots"


@pytest.fixture
def driver():
    """Chrome driver. Headless by default; set HEADED=1 to watch the browser."""
    options = Options()
    if os.getenv("HEADED") != "1":
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1400,900")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Keep Chrome's password-manager popups from covering the page.
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        },
    )
    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()


@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    page.open()
    return page


@pytest.fixture
def inventory_page(login_page):
    """Standard user, already logged in and sitting on the inventory page."""
    return login_page.login(config.STANDARD_USER, config.PASSWORD)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Save a screenshot when a test fails."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        drv = item.funcargs.get("driver")
        if drv is not None:
            SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
            safe_name = item.nodeid.replace("/", "_").replace("::", "__")
            drv.save_screenshot(str(SCREENSHOT_DIR / f"{safe_name}.png"))
