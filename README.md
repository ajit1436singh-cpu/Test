# Python Playwright Behave BDD UI Automation

A reusable browser UI automation framework built with [Playwright for Python](https://playwright.dev/python/) and [Behave](https://behave.readthedocs.io/). Test scenarios are written in Gherkin, while step definitions use Playwright’s synchronous Python API.

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

Configure the application under test in `.env`:

```dotenv
BASE_URL=https://your-application.example.com
HEADLESS=true
PLAYWRIGHT_TIMEOUT_MS=10000
IGNORE_HTTPS_ERRORS=false
```

## Run the BDD suite

Run all scenarios:

```bash
behave
```

Run smoke scenarios only:

```bash
behave --tags=smoke
```

Run with a visible browser for debugging:

```bash
HEADLESS=false behave --tags=smoke
```

Behave writes screenshots and HTML snapshots to `test-results/` when a scenario fails.

## Add a new scenario

Add a Gherkin scenario to a feature file under `features/`:

```gherkin
Feature: Search

  @regression
  Scenario: Search returns matching results
    Given I open the application
    When I navigate to "/search"
    Then I should see text "Search"
```

Implement additional steps in `features/steps/`. Prefer accessible and stable locators such as roles, labels, and test IDs. Keep credentials out of source control; use environment variables or GitHub Actions secrets for authenticated flows.

## Continuous integration

The workflow at `.github/workflows/playwright.yml` installs Python, Behave, Playwright, and Chromium, then runs `behave --tags=smoke`. Create a repository secret named `BASE_URL` under **Settings → Secrets and variables → Actions** before relying on the workflow.

## Project structure

```text
.
├── .env.example
├── .github/workflows/playwright.yml
├── behave.ini
├── features/
│   ├── environment.py
│   ├── smoke.feature
│   └── steps/ui_steps.py
├── requirements.txt
└── README.md
```

## Framework architecture

The framework follows the requested layered structure. Gherkin scenarios live under `features/`, page objects under `pages/`, stable selectors under `locators/`, reusable browser and configuration utilities under `utilities/`, and runtime settings under `config/config.ini`. The Behave hooks create and close the browser per scenario and save a screenshot plus HTML snapshot under `test-results/` when a scenario fails.

The default SauceDemo account is configured in `config/config.ini` for this public demo application. For another environment, override `BASE_URL`, `SAUCE_USERNAME`, and `SAUCE_PASSWORD` through `.env` or CI secrets. Real credentials must never be committed.

The smoke suite can be executed with:

```bash
behave --tags=smoke
```

The current smoke test validates opening the site, logging in with the standard user, reaching the inventory page, and seeing the Sauce Labs Backpack product.
