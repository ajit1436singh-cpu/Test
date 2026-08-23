from __future__ import annotations

from behave import then, when


@when("I log in to SauceDemo as the standard user")
def step_login_as_standard_user(context) -> None:
    context.login_page.login(
        str(context.settings["username"]),
        str(context.settings["password"]),
    )


@then("the inventory page should be displayed")
def step_inventory_page_should_be_displayed(context) -> None:
    context.inventory_page.assert_displayed()


@then('the inventory should contain the product "{product_name}"')
def step_inventory_should_contain_product(context, product_name: str) -> None:
    context.inventory_page.assert_product_present(product_name)
