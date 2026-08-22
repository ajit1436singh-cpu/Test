from behave import given, then, when
from playwright.sync_api import expect


@when("I log in to SauceDemo as the standard user")
def step_login_as_standard_user(context) -> None:
    context.page.get_by_placeholder("Username").fill("standard_user")
    context.page.get_by_placeholder("Password").fill("secret_sauce")
    context.page.get_by_role("button", name="Login").click()


@then("the inventory page should be displayed")
def step_inventory_page_should_be_displayed(context) -> None:
    expect(context.page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(context.page.get_by_text("Products", exact=True)).to_be_visible()


@then('the inventory should contain the product "{product_name}"')
def step_inventory_should_contain_product(context, product_name: str) -> None:
    expect(context.page.get_by_text(product_name, exact=True)).to_be_visible()
