Feature: Paramaterizing tests in Pytest BDD

  Scenario: Check varities of fruit
    Given There are 3 varieties of fruit
    When We add a same variety of fruit
    Then There is same count of varieties
    But If we add a different variety of fruit
    Then The count of varieties increases to 4