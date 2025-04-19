  Feature: Fruit Consumption Parameterization

    Scenario Outline: Eating multiple fruits in sequence
      Given We have <initial> fruits
      When I eat <eat1> fruits
      And I eat <eat2> fruits
      Then I should have <remaining> fruits

      Examples:
        | initial | eat1 | eat2 | remaining |
        | 5       | 3    | 2    | 0         |
        | 4       | 2    | 2    | 0         |
        | 10      | 4    | 3    | 3         |