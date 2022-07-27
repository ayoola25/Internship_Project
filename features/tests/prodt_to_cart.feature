# Created by EZ-Trainer at 5/9/2022
Feature: Test for Added Product

 Scenario: Verify that user can add product to the cart
   Given Open GetTop page
   When Click on Product Link
   And Click on first product
   And Click on Add to cart button
   And Open View Cart page
   Then Verify cart has 1 item(s)