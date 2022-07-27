# Created by EZ-Trainer at 6/13/2022
Feature: Tests for iPhone Link Functionality

  Scenario: Verify that iPhone 12 button on the Iphone Item drop down is not clickable
    Given Open GetTop page
    When Hover over IPHONE link
    And Click on iPhone 12 button
    Then Verify user can click iPhone 12 button