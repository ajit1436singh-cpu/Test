from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from playwright.sync_api import Browser, BrowserContext, Page, Playwright, sync_playwright


ROOT_DIR = Path(__file__).resolve().parents[1]
ARTIFACTS_DIR = ROOT_DIR / "test-results"
load_dotenv(ROOT_DIR / ".env")


def before_all(context) -> None:
    context.base_url = os.getenv("BASE_URL", "").strip().rstrip("/")
    if not context.base_url:
        raise RuntimeError("BASE_URL must be set to the application URL before running Behave")

    context.playwright: Playwright = sync_playwright().start()
    headless = os.getenv("HEADLESS", "true").lower() not in {"0", "false", "no"}
    context.browser: Browser = context.playwright.chromium.launch(headless=headless)


def before_scenario(context, scenario) -> None:
    context.browser_context: BrowserContext = context.browser.new_context(
        viewport={"width": 1440, "height": 900},
        ignore_https_errors=os.getenv("IGNORE_HTTPS_ERRORS", "false").lower() == "true",
    )
    context.page: Page = context.browser_context.new_page()
    context.page.set_default_timeout(int(os.getenv("PLAYWRIGHT_TIMEOUT_MS", "10000")))


def after_scenario(context, scenario) -> None:
    if scenario.status == "failed" and hasattr(context, "page"):
        ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
        safe_name = "".join(char if char.isalnum() else "_" for char in scenario.name).strip("_")
        context.page.screenshot(path=str(ARTIFACTS_DIR / f"{safe_name}.png"), full_page=True)
        (ARTIFACTS_DIR / f"{safe_name}.html").write_text(context.page.content(), encoding="utf-8")

    if hasattr(context, "browser_context"):
        context.browser_context.close()


def after_all(context) -> None:
    if hasattr(context, "browser"):
        context.browser.close()
    if hasattr(context, "playwright"):
        context.playwright.stop()
