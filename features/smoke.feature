Feature: Application availability
  As a user
  I want the application to be reachable
  So that I can use its core functionality

  @smoke @chromium
  Scenario: Application loads successfully
    Given I open the application
    Then the page should be displayed
    And the page title should not be empty
