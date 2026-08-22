from __future__ import annotations

import re
from urllib.parse import urljoin

from behave import given, then, when
from playwright.sync_api import expect


@given("I open the application")
def step_open_application(context) -> None:
    context.page.goto(context.base_url, wait_until="domcontentloaded")


@when('I navigate to "{path}"')
def step_navigate_to(context, path: str) -> None:
    target = urljoin(f"{context.base_url}/", path)
    context.page.goto(target, wait_until="domcontentloaded")


@then("the page should be displayed")
def step_page_should_be_displayed(context) -> None:
    expect(context.page.locator("body")).to_be_visible()


@then("the page title should not be empty")
def step_title_should_not_be_empty(context) -> None:
    expect(context.page).to_have_title(re.compile(r".+"))


@then('I should see text "{text}"')
def step_should_see_text(context, text: str) -> None:
    expect(context.page.get_by_text(text, exact=True)).to_be_visible()
