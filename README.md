# Sauce Demo UI Test Framework

UI test automation framework for [saucedemo.com](https://www.saucedemo.com/), a public demo store. Built with Python, Selenium WebDriver, and pytest using the Page Object Model. Tests run in headless Chrome on every push through GitHub Actions.

## What was tested

17 tests across four areas:

| Area | Coverage |
|---|---|
| Login | Valid login and logout, locked-out user error, wrong password error, empty username error, empty password error |
| Inventory | Sort by price (low to high), sort by name (A to Z), add item updates cart badge, add multiple items, remove item clears badge |
| Cart | Added items appear in cart, cart persists across navigation, remove item from cart |
| Checkout | Complete a two-item order and see the confirmation, missing first name error, missing postal code error, reset app state clears the cart |

Tests are tagged `smoke` (core flows) or `regression` (full coverage).

## Tools

- Python 3
- Selenium 4 (Selenium Manager handles the Chrome driver)
- pytest with `pytest-html` for the report
- GitHub Actions for CI

## Project structure

```
pages/            Page objects: base, login, inventory, cart, checkout
tests/            Test files, one per area
conftest.py       Driver and login fixtures, failure screenshots
config.py         URLs and the demo credentials published on the login page
pytest.ini        Markers and report options
.github/workflows/ci.yml
```

## Design notes

- Page Object Model: locators and page actions live in `pages/`, tests contain only steps and assertions.
- Explicit waits only (`WebDriverWait`), no `sleep`.
- Each test starts a fresh browser, so tests do not depend on each other.
- A screenshot is saved to `reports/screenshots/` whenever a test fails.

## How to run

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

pytest                           # all tests, headless
pytest -m smoke                  # smoke tests only
HEADED=1 pytest                  # watch the browser (Windows PowerShell: $env:HEADED=1; pytest)
```

Requires Google Chrome. The HTML report is written to `reports/report.html`.

## Continuous integration

`.github/workflows/ci.yml` runs the full suite on every push to `main` and every pull request, then uploads the HTML report and any failure screenshots as a build artifact.

## Results

![CI run passing](docs/Screenshot%202026-10-19%20125940.png)
