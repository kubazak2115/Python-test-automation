# QA automated Test Suite

Automated test suite covering UI (Selenium) and API (requests) testing.
## Stack

| Tool | Purpose |
|---|---|
| `pytest` | Test runner, fixtures, markers |
| `selenium` | Browser automation (Chrome) |
| `requests` | HTTP/API testing |
| `jsonschema` | JSON schema validation |
| `pytest-html` | HTML test reports |
| `webdriver-manager` | Auto ChromeDriver install |

## Project structure

```
main-/
├── tests/
│   ├── ui/
│   │  └──test_login.py 
│   └── api/
├── pages/                       
│   ├── login_page.py
│   └── inventory_page.py
├── conftest.py                  
├── pytest.ini                   
├── reports/                    
└── requirements.txt
```

## Setup

```bash
git clone <repo-url>

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

## Running tests

```bash
# All tests + HTML report
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

## HTML Report

After running, open `reports/report.html` in your browser.

## Target site

UI tests run against **[SauceDemo](https://www.saucedemo.com)** —
a demo e-commerce app maintained by Sauce Labs specifically for test automation practice.

API tests run against **[JSONPlaceholder](https://jsonplaceholder.typicode.com)** —
a free public REST API for prototyping and testing.