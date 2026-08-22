from __future__ import annotations

import os
from collections.abc import Generator
from pathlib import Path

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page


ROOT_DIR = Path(__file__).resolve().parents[1]
load_dotenv(ROOT_DIR / ".env")


@pytest.fixture(scope="session")
def base_url() -> str:
    """Return the application URL configured by BASE_URL."""
    value = os.getenv("BASE_URL", "").strip()
    if not value:
        pytest.skip("Set BASE_URL to the application under test before running UI tests")
    return value.rstrip("/")


@pytest.fixture
def app_page(page: Page, base_url: str) -> Generator[Page, None, None]:
    """Navigate to the configured application and return the Playwright page."""
    page.goto(base_url, wait_until="domcontentloaded")
    yield page
