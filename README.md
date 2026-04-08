# Python test automation

Automated test suite for [Sauce Demo](https://www.saucedemo.com) (UI) and [JSONPlaceholder](https://jsonplaceholder.typicode.com) (API)

## Tech Stack

| Tool | Purpose |
|------|---------|
| `pytest` | Test runner & framework |
| `selenium` | UI / browser automation |
| `requests` | REST API testing |
| `jsonschema` | JSON schema validation |
| `pytest-html` | HTML test reports |
| `webdriver-manager` | Automatic ChromeDriver management |

## Project Structure

```
qa-portfolio/
├── tests/
│   ├── ui/
│   │   ├── test_login.py       # Login flows, edge cases, parametrized tests
│   │   ├── test_cart.py        # Add/remove items, cart state, navigation
│   │   └── test_checkout.py    # Full purchase flow, form validation, E2E
│   └── api/
│       ├── test_endpoints.py   # GET, POST, PUT, DELETE — status codes
│       └── test_schema.py      # JSON schema validation with jsonschema
├── pages/                      # Page Object Model
│   ├── base_page.py            # Base class — shared methods
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── conftest.py                 # Fixtures: driver setup, login, teardown
├── pytest.ini                  # Markers, HTML report config
├── reports/                    # Auto-generated HTML reports
└── requirements.txt
```

## Setup

```bash
git clone 
pip install -r requirements.txt
```

> Requires Python 3.10+ and Google Chrome installed.

## Running Tests

```bash
# Full suite + HTML report
pytest

# Only smoke tests (fast, critical path)
pytest -m smoke

# Only UI tests
pytest -m ui

# Only API tests
pytest -m api

# Specific file
pytest tests/ui/test_login.py -v
```

## Test Markers

| Marker | Description |
|--------|-------------|
| `@pytest.mark.smoke` | Critical path |
| `@pytest.mark.regression` | Full regression suite |
| `@pytest.mark.ui` | Selenium UI tests |
| `@pytest.mark.api` | REST API tests |

## What's Tested

**UI — Sauce Demo**
- Login: valid users, locked user, empty fields, SQL injection, XSS, parametrized users
- Cart: adding/removing items, badge count, cart persistence, navigation
- Checkout: form validation, price calculation, E2E purchase flow

**API — JSONPlaceholder**
- GET, POST, PUT, DELETE endpoints with status code assertions
- JSON schema validation for posts, comments and users
- Parametrized tests across multiple resource IDs

## Reports

After running `pytest`, open `reports/report.html` in your browser for a full HTML report with pass/fail status, test durations, and error details.

---
