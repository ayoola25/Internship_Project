# Created by EZ-Trainer at 6/30/2022
Feature: Test to show Cart Functionality

   Scenario: 'Your cart is currently empty' shown if no product added
      Given Open GitTop page
      When Click on cart_icon
      Then Verify Your cart is currently empty text present