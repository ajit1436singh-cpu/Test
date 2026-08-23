from __future__ import annotations

from playwright.sync_api import Browser, BrowserContext, Page, Playwright


class BrowserManager:
    def __init__(self, playwright: Playwright, settings: dict[str, object]) -> None:
        self._playwright = playwright
        self._settings = settings
        self.browser: Browser | None = None
        self.context: BrowserContext | None = None
        self.page: Page | None = None

    def start(self) -> Page:
        headless = bool(self._settings["headless"])
        self.browser = self._playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context(
            viewport={
                "width": int(self._settings["viewport_width"]),
                "height": int(self._settings["viewport_height"]),
            },
            ignore_https_errors=bool(self._settings["ignore_https_errors"]),
        )
        self.page = self.context.new_page()
        self.page.set_default_timeout(int(self._settings["timeout_ms"]))
        return self.page

    def close(self) -> None:
        if self.context:
            self.context.close()
        if self.browser:
            self.browser.close()
