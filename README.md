# Python Playwright UI Automation

A reusable Python UI automation starter project built with [Playwright](https://playwright.dev/python/) and [pytest](https://docs.pytest.org/). The target application is configured through `BASE_URL`, so the framework can be connected to any web application without changing the test runner.

## Requirements

- Python 3.10 or newer
- A reachable web application URL
- Internet access when installing dependencies and Playwright browsers

## Setup

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m playwright install --with-deps chromium
cp .env.example .env
```

Set the application URL in `.env`:

```dotenv
BASE_URL=https://your-application.example.com
```

## Run the tests

Run the complete suite in headless mode:

```bash
pytest
```

Run only smoke tests:

```bash
pytest -m smoke
```

Run with a visible browser and slow motion while debugging:

```bash
PWDEBUG=1 pytest -m smoke
```

Generate an HTML report:

```bash
pytest --browser chromium --tracing retain-on-failure --video retain-on-failure --screenshot only-on-failure
```

## Adding application-specific coverage

Add tests under `tests/`. Prefer accessible, stable locators such as `get_by_role`, `get_by_label`, and `get_by_test_id`. Replace the generic assertions in `tests/test_smoke.py` with assertions that describe the application’s real critical path.

For authentication, use a dedicated non-production account and store secrets in environment variables or CI secrets. Do not commit credentials to the repository.

## Continuous integration

The GitHub Actions workflow in `.github/workflows/playwright.yml` installs Python, dependencies, Chromium, and runs the suite using the repository secret `BASE_URL`. Add that secret under **Settings → Secrets and variables → Actions** before relying on CI results.

## Project structure

```text
.
├── .env.example
├── .github/workflows/playwright.yml
├── pytest.ini
├── requirements.txt
├── tests/
│   ├── conftest.py
│   └── test_smoke.py
└── README.md
```
