Feature: Fixture and BDD Background on python set datatype

  Background: Setting up data for test
    Given A datatype set
    And The Set is not empty


  Scenario: Adding elements to a set
    Given Set has 3 elements
    When We add 2 elements to the set
    Then Set now has 5 elements