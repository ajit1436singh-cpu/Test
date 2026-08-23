from __future__ import annotations

import logging
import re
from pathlib import Path

from dotenv import load_dotenv
from playwright.sync_api import Playwright, sync_playwright

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utilities.browser_manager import BrowserManager
from utilities.config_reader import ROOT_DIR, load_settings


load_dotenv(ROOT_DIR / ".env")


def before_all(context) -> None:
    context.settings = load_settings()
    context.base_url = str(context.settings["base_url"])
    if not context.base_url:
        raise RuntimeError("BASE_URL must be configured before running Behave")
    logging.basicConfig(level=getattr(logging, str(context.settings["log_level"]).upper(), logging.INFO))
    context.playwright: Playwright = sync_playwright().start()


def before_scenario(context, scenario) -> None:
    context.browser_manager = BrowserManager(context.playwright, context.settings)
    context.page = context.browser_manager.start()
    context.login_page = LoginPage(context.page, context.base_url)
    context.inventory_page = InventoryPage(context.page, context.base_url)


def after_scenario(context, scenario) -> None:
    if scenario.status == "failed" and hasattr(context, "page"):
        artifacts_dir = Path(context.settings["artifacts_dir"])
        artifacts_dir.mkdir(parents=True, exist_ok=True)
        safe_name = re.sub(r"[^A-Za-z0-9_-]+", "_", scenario.name).strip("_") or "failed_scenario"
        context.page.screenshot(path=str(artifacts_dir / f"{safe_name}.png"), full_page=True)
        (artifacts_dir / f"{safe_name}.html").write_text(context.page.content(), encoding="utf-8")
    if hasattr(context, "browser_manager"):
        context.browser_manager.close()


def after_all(context) -> None:
    if hasattr(context, "playwright"):
        context.playwright.stop()
