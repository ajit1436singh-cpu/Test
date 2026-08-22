import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.smoke
@pytest.mark.chromium
def test_application_loads(app_page: Page) -> None:
    """Verify that the configured application responds and renders a document."""
    expect(app_page).to_have_title(re.compile(r".+"))
    expect(app_page.locator("body")).to_be_visible()


@pytest.mark.smoke
@pytest.mark.chromium
def test_application_has_primary_content(app_page: Page) -> None:
    """Template for a meaningful landing-page assertion.

    Replace the generic body assertion with a stable locator from the application,
    such as get_by_role("heading", name="Dashboard") or a data-testid.
    """
    expect(app_page.locator("body")).not_to_be_empty()
