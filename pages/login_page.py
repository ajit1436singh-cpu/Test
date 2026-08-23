from __future__ import annotations

from playwright.sync_api import Page, expect

from locators.saucedemo_locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)
        self.username = page.locator(LoginLocators.USERNAME)
        self.password = page.locator(LoginLocators.PASSWORD)
        self.login_button = page.locator(LoginLocators.LOGIN_BUTTON)

    def login(self, username: str, password: str) -> None:
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def assert_login_error(self, message: str) -> None:
        expect(self.page.locator(LoginLocators.ERROR)).to_contain_text(message)
