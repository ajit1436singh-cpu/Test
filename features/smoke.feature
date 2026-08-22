Feature: SauceDemo smoke coverage
  As a user
  I want to verify the public SauceDemo storefront
  So that the core login and inventory flow remains available

  @smoke @chromium
  Scenario: Standard user can open the inventory
    Given I open the application
    When I log in to SauceDemo as the standard user
    Then the inventory page should be displayed
    And the inventory should contain the product "Sauce Labs Backpack"
