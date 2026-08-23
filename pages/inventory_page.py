from __future__ import annotations

from playwright.sync_api import Page, expect

from locators.saucedemo_locators import InventoryLocators
from pages.base_page import BasePage


class InventoryPage(BasePage):
    def assert_displayed(self) -> None:
        expect(self.page).to_have_url(f"{self.base_url}/inventory.html")
        expect(self.page.locator(InventoryLocators.PAGE_TITLE)).to_have_text("Products")

    def assert_product_present(self, product_name: str) -> None:
        expect(self.page.locator(InventoryLocators.PRODUCT_NAMES).filter(has_text=product_name)).to_be_visible()
