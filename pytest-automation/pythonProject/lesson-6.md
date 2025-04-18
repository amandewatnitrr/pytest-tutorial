from pytest_bdd import scenarios

# Pytest - BDD: Behaviour Driven Development

- Let's first start by understanding what BDD is.

> [!IMPORTANT]
> Behavior-Driven Development (BDD) is a collaborative software development methodology that bridges the gap between technical and non-technical stakeholders by focusing on the desired behavior of a system from the user's perspective. 
> It extends Test-Driven Development (TDD) by emphasizing shared understanding through natural language scenarios.

- In TDD(Test Driven Development), we start by writing the tests for our features even before implementing the 
  feature, or even before starting to code the actual feature.
- In BDD, we start by writing the behaviour of the feature in plain-language like English. In this we first write 
  the behaviour of the system from the end user's perspective or the customer's perspective in a `feature` file

### Key Component of BDD:

- User Stories
  - Written in plain-language

- Scenarios
  - Structured using Gherkin Syntax
	
	```Ghyrkan
	Scenario: Successful password reset  
	  Given a registered user navigates to the login page  
	  When they click "Forgot Password" and enter a valid email  
	  Then a reset link is sent to their email  
    ```
 
 - Keywords: `Given` (preconditions), `When` (actions), `Then` (outcomes).

- Automated Tests

  - Tools like Cucumber, Behave, or pytest-bdd map Gherkin scenarios to executable code.

### Why BDD Testing is needed??

- Shared Clarity: Aligns developers, testers, and business teams on requirements, reducing misinterpretations.
- User-Centric Validation: Tests validate what the system should do (behavior) rather than how it does it (implementation).
- Early Defect Detection: Scenarios are defined upfront, exposing gaps in requirements before coding begins.
- Living Documentation: Gherkin scenarios serve as up-to-date, human-readable documentation.
- Automation Efficiency: Executable scenarios enable continuous testing and regression checks.

### When to use BDD ??

- Complex projects with multiple stakeholders.
- Teams needing clear, shared requirements.
- Systems requiring end-to-end validation of user journeys.


### Pytest: Terms and Rules

- In Pytest, BDD is a plugin of the pytest. We need to install `pytest-bdd` using the command:

	```bash
	pip install pytest-bdd
	```
 
- It's not only the BDD Framework, but other pytest features, and all the other pytest functionalities available 
  with you to write your test in much easier way. 

- Next, we need to know about is Gherkin. Gherkin is a simple programming language. It is used to write the feature 
  file. It is written in Simple English language. The code is written in `.feature` file. Using this language, we 
  write the behaviour or scenarios of our test/code.

- The Step definitions are written in Python Language. It's a python function , those functions are decorated by the 
  matching string, as shown below:

	```python
	@given("The account balance is 100.")
	def current_balance():
		pytest.amt = 100
	```
 
- The step is glued to the step definition, and these definition are written in python modules or python files.
- Only 1 feature is allowed per feature file. We cannot have multiple features in a single feature file, but we can 
  have multiple scenarios in a single feature file.
- The Project structuring for `pytest-bdd` is quite flexible, so the step-definiton modules need not to be same as 
  feature file names. We can have a different name for the feature file, and different name for the test modules.
- Scenarios, explicitly be declared in the test modules. That's hwo we will be able to connect between the scenarios 
  and the step-definiton or our test functions.

## Getting started with BDD Testing

- Let's start by creating a proper file structure for our BDD Testing. In our, `pytest_topics` folder we have 
  created a sub directory called `bdd_test`, inside which we have another sub directory called `feature_dir`, here 
  we store all the `*.feature` files.

  ![](./imgs/Screenshot%202025-04-18%20at%204.46.13.png)

- We will start by learning to write a feature file. We have created a file name `test_1.feature`.

  `test_1.feature`
  
  ```feature
  Feature: Bank Transactions
      Tests pertaining to banking transactions like withdrawal, deposit.
  
    Scenario: Withdrawal of Money
      Given The account balance is 100
      When The account holder withdraws 30
      Then The account balance remaining should be 70
  ```
 
- Now, create a test file setting up the scenario, given the conditions and, the expected outcomes in the python 
  test file. 

  `test_bdd_1.py`
  
  ```python
  from pytest_bdd import scenario, scenarios, given, when, then
  from pathlib import Path
  import pytest
  
  featureFileDir = 'feature_dir'
  featureFile = 'test_1.feature'
  
  BASE_DIR = Path(__file__).resolve().parent
  FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)
  
  def pytest_configure():
      pytest.AMT = 0
  
  
  @scenario(FEATURE_FILE, 'Withdrawal of Money')
  def test_withdrawal():
      print(f"Test: Withdrawal of Money - Successfull")
      pass
  
  @given('The account balance is 100')
  def starting_balance():
      pytest.AMT = 100
      print(f"\nStarting account balance {pytest.AMT}")
  
  @when('The account holder withdraws 30')
  def withdrawal_request():
      pytest.AMT -= 30
      print("\nAmount deducted = 30")
  
  @then('The account balance remaining should be 70')
  def check_balance():
      print(f"\nRemaining Amount = {pytest.AMT}")
      assert pytest.AMT == 70
  ```
  
- The step-definitions in the python file, and feature file must match each other.

- Once, you execute the test, you get the following output:

  ```bash
  $  pytest -v -s test_bdd_1.py                        ✔  pythonProject   at 16:33:41  
  =================================================================== test session starts ===================================================================
  platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python
  cachedir: .pytest_cache
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  configfile: pytest.ini
  plugins: bdd-8.1.0
  collected 1 item                                                                                                                                          
  
  test_bdd_1.py::test_withdrawal 
  Starting account balance 100
  
  Amount deducted = 30
  
  Remaining Amount = 70
  Test: Withdrawal of Money - Successfull
  PASSED
  
  ==================================================================== 1 passed in 0.01s ====================================================================
  ```
  
- Here, you can clearly, see the step-definition being followed in sequence. This is how we can execute our BDD Tests.

- Let's add another scenario, to learn from.

  `test_1.feature`
  
  ```feature
  Feature: Bank Transactions
      Tests pertaining to banking transactions like withdrawal, deposit.
  
    Scenario: Withdrawal of Money
      Given The account balance is 100
      When The account holder withdraws 30
      Then The account balance remaining should be 70
  
    Scenario: Removal of items from set
      Given A set of 3 fruits
      When We remove a fruit from the set
      Then The set will have 2 fruits
  ```
  
- Write the tests in python to test the scenario.

  `test_bdd_1.py`
  
  ```python
  from pytest_bdd import scenario, scenarios, given, when, then
  from pathlib import Path
  import pytest
  
  
  featureFileDir = 'feature_dir'
  featureFile = 'test_1.feature'
  
  BASE_DIR = Path(__file__).resolve().parent
  FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)
  
  def pytest_configure():
      pytest.AMT = 0
  
  
  @scenario(FEATURE_FILE, 'Withdrawal of Money')
  def test_withdrawal():
      print(f"Test: Withdrawal of Money - Completed")
      pass
  
  
  @given('The account balance is 100')
  def starting_balance():
      pytest.AMT = 100
      print(f"\nStarting account balance {pytest.AMT}")
  
  
  @when('The account holder withdraws 30')
  def withdrawal_request():
      pytest.AMT -= 30
      print("\nAmount deducted = 30")
  
  
  @then('The account balance remaining should be 70')
  def check_balance():
      print(f"\nRemaining Amount = {pytest.AMT}")
      assert pytest.AMT == 70
  
  @scenario(FEATURE_FILE,"Removal of items from set")
  def test_itemRemovalFromSet():
      print("Test: Removal of Item from Test - Completed")
      pass
  
  @given("A set of 3 fruits",target_fixture="fruits")
  def setOfFruits():
      fruits = {"apple", "mango", "banana"}
      print(f"\nFruits in set: {fruits}")
      return fruits
  
  # To use the paramater fruits, we need to define special parameter called `target_fixture`.
  
  @when("We remove a fruit from the set")
  def removeFruits(fruits):
      print(f"\nFruit removed: {fruits.pop()}")
      print(f"\nRemaining Fruits: {fruits}")
  
  @then("The set will have 2 fruits")
  def remainderFruits(fruits):
      try:
          assert len(fruits) == 2
          print("\nThere are now 2 fruits in set.")
      except Exception as e:
          print(f"\nUnknown error occurred: {e}")
  
  ```

- In this case, here you can see, instead of initializing a new variable, we have used a special parameter called 
  `target_fixture`. The `target_fixture` parameter, is used in the `@given` decorator to export, and share the 
  variable with other functions and test functions.

- Once, you execute this, you see the following output:

  ```bash
  $  pytest -v -s test_bdd_1.py                        ✔  pythonProject   at 16:37:22  
  =================================================================== test session starts ===================================================================
  platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python
  cachedir: .pytest_cache
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  configfile: pytest.ini
  plugins: bdd-8.1.0
  collected 2 items                                                                                                                                         
  
  test_bdd_1.py::test_withdrawal 
  Starting account balance 100
  
  Amount deducted = 30
  
  Remaining Amount = 70
  Test: Withdrawal of Money - Completed
  PASSED
  test_bdd_1.py::test_itemRemovalFromSet 
  Fruits in set: {'apple', 'mango', 'banana'}
  
  Fruit removed: apple
  
  Remaining Fruits: {'mango', 'banana'}
  
  There are now 2 fruits in set.
  Test: Removal of Item from Test - Completed
  PASSED
  
  ==================================================================== 2 passed in 0.01s ====================================================================
  ```
  
## `scenarios` vs `scenario` decorator

- So, far we have used the `scenario` decorator, where we have to write for each `scenario` individually. But, we 
  can also do it another way where we define the whole feature file. Instead of needing to write a seprate scenario 
  for each of the test, we can just define the scenario file, and it will collect everything from that whole file, 
  and it will run.

- For that we can use the `scenarios` decorator. We can use this in following way:

  ```python
  scenarios(FEATURE_FILE)
  ```
  
- Here, we are not pointing to each scenario individually, but rather at the whole feature file itself. Or, we can 
  also point to the folder that will also work because the linking which is happening test module and the test 
  function and, the test scenario is covered by `given`, `when` and `then` step-definitions.

> [!TIP]
> The best practice is to specify feature file, instead of folder name.

- So, let's suppose we comment out our scenario test functions from the bdd test python file, and let's try 
  executing it.

  `test_bdd_1.py`
  
  ```python
  from pytest_bdd import scenario, scenarios, given, when, then
  from pathlib import Path
  import pytest
  
  
  featureFileDir = 'feature_dir'
  featureFile = 'test_1.feature'
  
  BASE_DIR = Path(__file__).resolve().parent
  FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)
  
  def pytest_configure():
      pytest.AMT = 0
  
  scenarios(FEATURE_FILE)
  
  # @scenario(FEATURE_FILE, 'Withdrawal of Money')
  # def test_withdrawal():
  #     print(f"Test: Withdrawal of Money - Completed")
  #     pass
  
  
  @given('The account balance is 100')
  def starting_balance():
      pytest.AMT = 100
      print(f"\nStarting account balance {pytest.AMT}")
  
  
  @when('The account holder withdraws 30')
  def withdrawal_request():
      pytest.AMT -= 30
      print("\nAmount deducted = 30")
  
  
  @then('The account balance remaining should be 70')
  def check_balance():
      print(f"\nRemaining Amount = {pytest.AMT}")
      assert pytest.AMT == 70
  
  # @scenario(FEATURE_FILE,"Removal of items from set")
  # def test_itemRemovalFromSet():
  #     print("Test: Removal of Item from Test - Completed")
  #     pass
  
  @given("A set of 3 fruits",target_fixture="fruits")
  def setOfFruits():
      fruits = {"apple", "mango", "banana"}
      print(f"\nFruits in set: {fruits}")
      return fruits
  
  # To use the paramater fruits, we need to define special parameter called `target_fixture`.
  
  @when("We remove a fruit from the set")
  def removeFruits(fruits):
      print(f"\nFruit removed: {fruits.pop()}")
      print(f"\nRemaining Fruits: {fruits}")
  
  @then("The set will have 2 fruits")
  def remainderFruits(fruits):
      try:
          assert len(fruits) == 2
          print("\nThere are now 2 fruits in set.")
      except Exception as e:
          print(f"\nUnknown error occurred: {e}")
  
  ```

  ```bash
  $ pytest -v -s test_bdd_1.py                                                 ✔  pythonProject   at 17:33:24  
  ============================================================================ test session starts =============================================================================
  platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python
  cachedir: .pytest_cache
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  configfile: pytest.ini
  plugins: bdd-8.1.0
  collected 2 items                                                                                                                                                            
  
  test_bdd_1.py::test_withdrawal_of_money 
  Starting account balance 100
  
  Amount deducted = 30
  
  Remaining Amount = 70
  PASSED
  test_bdd_1.py::test_removal_of_items_from_set 
  Fruits in set: {'apple', 'mango', 'banana'}
  
  Fruit removed: apple
  
  Remaining Fruits: {'mango', 'banana'}
  
  There are now 2 fruits in set.
  PASSED
  
  ============================================================================= 2 passed in 0.01s ==============================================================================
  ```
  
- So, the tests are still being covered. As we can see here: `test_withdrawal_of_money`, 
  `test_removal_of_items_from_set` it's generating using the `Scenario` in the feature file, and identifying for us 
  which specific BDD Test Cases have been successfully covered.

## Pytest BDD & Fixtures

- A important note to consider while going through section is, nothing changes for the fixtures and, everything 
  remains same.
- Let's understand this using an example. In this example, we will take a set of strings. The test will be to check 
  the length of the updated set, if it matches the expected length or not.

  `test_fixture.feature`
  
  ```feature
  Feature: Fixture and BDD Background on python set datatype
  
    Scenario: Adding elements to a set
      Given Set has 3 elements
      When We add 2 elements to the set
      Then Set now has 5 elements
  ```

  `test_baddFixtures.py`
  
  ```python
  from pytest_bdd import scenario, scenarios, when, then, given
  from pathlib import Path
  import pytest
  
  featureFileDir = 'feature_dir'
  featureFile = 'test_fixture.feature'
  
  BASE_DIR = Path(__file__).resolve().parent
  FEATURE_FILE=BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)
  
  scenarios(FEATURE_FILE)
  
  @pytest.fixture()
  def setup_set():
      countries = {"India", "China", "US"}
      print(f"Forming Set: {countries}")
      return countries
  
  @given("Set has 3 elements",target_fixture="setup_set")
  def setOfEle(setup_set):
      if len(setup_set) == 0:
          pytest.xfail("Set is empty.")
      elif len(setup_set) > 3:
          while len(setup_set) > 3:
              setup_set.pop()
      return setup_set
  
  @when("We add 2 elements to the set")
  def addEleToSet(setup_set):
      setup_set.add("UK")
      setup_set.add("Russia")
      print("\nAdded 2 elements to the set")
  
  @then("Set now has 5 elements")
  def checkSet(setup_set):
      print(f"\nSet has {len(setup_set)} elements.")
      assert len(setup_set) == 5
      print("\nSet Length check test completed.")
  ```
  
- Here, you can see that how we have defined a fixture `setup_set`. For the `given` decorator, we use it to 
  initialize the set, making sure, the set is of the proper size as expected. We use the `target_fixture` parameter 
  of the `given` decorator to share the variable value with `when` and `than` decorators. Following that we modify 
  the set, and check if the length is same as the expected length.

  If you run the test, you will see the following output:

  ```bash
  $ pytest -v -s test_bddFixtures.py        ✔  pythonProject   at 17:35:21  
  =========================================================== test session starts ===========================================================
  platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python
  cachedir: .pytest_cache
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  configfile: pytest.ini
  plugins: bdd-8.1.0
  collected 1 item                                                                                                                          
  
  test_bddFixtures.py::test_adding_elements_to_a_set Forming Set: {'US', 'India', 'China'}
  
  Added 2 elements to the set
  
  Set has 5 elements.
  
  Set Length check test completed.
  PASSED
  
  ============================================================ 1 passed in 0.01s ============================================================
  ```

## Pytest-BDD: About Background

- Occasionally, we'll find ourselves repeating the same `Given` steps in all of the scenarios in a `Feature`. Since, 
  it might be repeated in every scenario, this is an indication that those steps are not essential to describe the 
  scenarios; they are incidental details. We can move such `Given` steps to the background, by grouping them under a 
  `Background` section.

- All the steps from background will be executed before all the scenario's own givens steps. This provides us with a 
  facility of preparing common setups for multiple scenarios using in a single section.

> [!NOTE]
> There is only `Given` step-definition that should be used in `Background` section, step-definitions `When` and 
> `Then` are prohibited because their purpose are related to actions and consuming outcomes, that is conflict with 
> `Background` aim - prepare system for tests or "put the system in a known state" as `Given` does it. The statement 
> above is applied for strict Gherkin mode, which is enabled by default.

- Let's try to understand this through an example:

  `test_fixture.feature`
  
  ```feature
  Feature: Fixture and BDD Background on python set datatype
  
    Background: Setting up data for test
      Given A datatype set
      And The Set is not empty
  
  
    Scenario: Adding elements to a set
      Given Set has 3 elements
      When We add 2 elements to the set
      Then Set now has 5 elements
  ```

  `test_bddFixtures.py`

  ```python
  from pytest_bdd import scenario, scenarios, when, then, given
  from pathlib import Path
  import pytest
  
  featureFileDir = 'feature_dir'
  featureFile = 'test_fixture.feature'
  
  BASE_DIR = Path(__file__).resolve().parent
  FEATURE_FILE=BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)
  
  scenarios(FEATURE_FILE)
  
  @pytest.fixture()
  def setup_set():
      countries = {"India", "China", "US", "Germany"}
      print(f"Forming Set: {countries}")
      return countries
  
  @given("A datatype set")
  def checkSetType(setup_set):
      print("\nChecking Set Type in background...")
      if not isinstance(setup_set,set):
          pytest.xfail("\nDatatype is not set.")
      else:
          print("\nDatatype is set.")
  
  @given("The Set is not empty")
  def setNotEmpty(setup_set):
      print("\nChecking set length in background...")
      if(len(setup_set)) <= 0:
          pytest.xfail("\nFailure expected. Set is empty or smaller than expected.")
      elif len(setup_set) == 3 :
          print("\nSet is of desired size.")
      else:
          print("\nSet is bigger than expected. pop() needed.")
  
  
  @given("Set has 3 elements",target_fixture="setup_set")
  def setOfEle(setup_set):
      if len(setup_set) == 0:
          pytest.xfail("Set is empty.")
      elif len(setup_set) > 3:
          while len(setup_set) > 3:
              setup_set.pop()
      return setup_set
  
  @when("We add 2 elements to the set")
  def addEleToSet(setup_set):
      setup_set.add("UK")
      setup_set.add("Russia")
      print("\nAdded 2 elements to the set")
  
  @then("Set now has 5 elements")
  def checkSet(setup_set):
      print(f"\nSet has {len(setup_set)} elements.")
      assert len(setup_set) == 5
      print("\nSet Length check test completed.")
  ```
  
- In the feature file as you can see, we have `Background` section covering the setup for us, checking if the data 
  is of required type, and does have a desired legnth, using the `2` given statements. So, the order of execution 
  now becomes:

  ```plainText
  Given(Scenario) -> Background -> When(scenario) -> Then(scenario)
  ```
  
- Once executed, you will see the following output for the pytest:

  ```bash
  $ pytest -v -s test_bddFixtures.py  ✔  pythonProject   at 20:12:23  
  =========================================================== test session starts ===========================================================
  platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python
  cachedir: .pytest_cache
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  configfile: pytest.ini
  plugins: bdd-8.1.0
  collected 1 item                                                                                                                          
  
  test_bddFixtures.py::test_adding_elements_to_a_set Forming Set: {'US', 'Germany', 'China', 'India'}
  
  Checking Set Type in background...
  
  Datatype is set.
  
  Checking set length in background...
  
  Set is bigger than expected. pop() needed.
  
  Added 2 elements to the set
  
  Set has 5 elements.
  
  Set Length check test completed.
  PASSED
  
  ============================================================ 1 passed in 0.01s ============================================================
  ```

## Paramaterizing in Pytest BDD

- Let's try to understand this through an example directly.

  `test_paramaterzie.feature`
  
  ```feature
  Feature: Paramaterizing tests in Pytest BDD
  
    Scenario: Check varities of fruit
      Given There are 3 varieties of fruit
      When We add a same variety of fruit
      Then There is same count of varieties
      But If we add a different variety of fruit
      Then The count of varieties increases to 4
  ```
  
  `test_bddParamaterize.py`
  
  ```python
  from pytest_bdd import scenario, scenarios, when, then, given, parsers
  from pathlib import Path
  import pytest
  
  featureFileDir = 'feature_dir'
  featureFile = 'test_paramaterzie.feature'
  
  BASE_DIR = Path(__file__).resolve().parent
  FEATURE_FILE=BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)
  
  scenarios(FEATURE_FILE)
  
  @given("There are 3 varieties of fruit",target_fixture="fruits")
  def exsistingFruits():
      fruits = {'apple', 'grapes', 'strawberry'}
      print(f"Fruits: {fruits}. There are total of {len(fruits)}")
      return fruits
  
  @when("We add a same variety of fruit")
  def addSameFruit(fruits):
      print("\nAdding a fruit that is already there in the set.")
      fruits.add("grapes")
  
  @then("There is same count of varieties")
  def same_count(fruits):
      print(f"There are still {len(fruits)} fruit varieties.")
      assert len(fruits) == 3
  
  
  @then("If we add a different variety of fruit")
  def addDiffFruit(fruits):
      print("\nTomato added to fruits")
      fruits.add("Tomato")
  
  @then(parsers.parse("The count of varieties increases to {count:d}"))
  def updated_count(fruits,count):
      print(f"\nThere are {count} varieties of fruits.")
      assert len(fruits) == count
  
  ```
  
- Here, you can see that for paramaterizing we have used, `parser.parse()` in the `then` decorator, wherein we have 
  mentioned the count of varieties of fruits as `{count:d}`, where `d` is the datatype for `digits`. And, contains 
  the value picked from the feature file.

- When you run this test, you get this kind of output.

  ```bash
  $ pytest -v -s test_bddParamaterize.py 
  ====================================================== test session starts ======================================================
  platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python
  cachedir: .pytest_cache
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  configfile: pytest.ini
  plugins: bdd-8.1.0
  collected 1 item                                                                                                                
  
  test_bddParamaterize.py::test_check_varities_of_fruit Fruits: {'apple', 'grapes', 'strawberry'}. There are total of 3
  
  Adding a fruit that is already there in the set.
  There are still 3 fruit varieties.
  
  Tomato added to fruits
  
  There are 4 varieties of fruits.
  PASSED
  
  ======================================================= 1 passed in 0.01s =======================================================
  ```
  
- Let's try to explore some more examples to understand benefits of Paramaterizing in BDD Tests.

  `test_paramaterzie.feature`
  
  ```feature
  Feature: Paramaterizing tests in Pytest BDD
  
    Scenario: Check varities of fruit
      Given There are 3 varieties of fruit
      When We add a same variety of fruit
      Then There is same count of varieties
      But If we add a different variety of fruit
      Then The count of varieties increases to 4
  
    Scenario: Paramaterize benefits
      Given We have 5 fruits
      When I eat 3 fruits
      And I eat 2 fruits
      Then I should have 0 fruits
  ```

  `test_bddParamaterize.py`
  
  ```python
  from pytest_bdd import scenario, scenarios, when, then, given, parsers
  from pathlib import Path
  import pytest
  from pytest_bdd.generation import print_missing_code
  
  featureFileDir = 'feature_dir'
  featureFile = 'test_paramaterzie.feature'
  
  BASE_DIR = Path(__file__).resolve().parent
  FEATURE_FILE=BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)
  
  scenarios(FEATURE_FILE)
  
  @given("There are 3 varieties of fruit",target_fixture="fruits")
  def exsistingFruits():
      fruits = {'apple', 'grapes', 'strawberry'}
      print(f"Fruits: {fruits}. There are total of {len(fruits)}")
      return fruits
  
  @when("We add a same variety of fruit")
  def addSameFruit(fruits):
      print("\nAdding a fruit that is already there in the set.")
      fruits.add("grapes")
  
  @then("There is same count of varieties")
  def same_count(fruits):
      print(f"There are still {len(fruits)} fruit varieties.")
      assert len(fruits) == 3
  
  
  @then("If we add a different variety of fruit")
  def addDiffFruit(fruits):
      print("\nTomato added to fruits")
      fruits.add("Tomato")
  
  @then(parsers.parse("The count of varieties increases to {count:d}"))
  def updated_count(fruits,count):
      print(f"\nThere are {count} varieties of fruits.")
      assert len(fruits) == count
  
  
  # Scenario: Paramaterize Benefits
  
  @given(parsers.parse("We have {count:d} fruits"),target_fixture="start_fruits")
  def exsistingFruits(count):
      return dict(start=count,eat = 0)
  
  @when(parsers.parse("I eat {eat:d} fruits"))
  def eat3ruits(start_fruits,eat):
      print(f"\nWe have eaten {eat} fruits.")
      start_fruits["eat"] += eat
  
  @then(parsers.parse("I should have {left:d} fruits"))
  def shouldHaveFruits(start_fruits,left):
      diff = start_fruits["start"] - start_fruits["eat"]
      print(f"\nWe have {diff} fruits remaining.")
      assert start_fruits["start"] - start_fruits["eat"] == left
  
  ```
  
- Here, you can see for the 2nd scenario in the feature file `test_paramaterzie.feature`, we have used the same 
  function in the python file `test_bddParamaterize.py` for the  `When` step-definition. Because, the only 
  difference there was the number.

- If you execute this, we see the following output:

  ```bash
  pytest -v -s test_bddParamaterize.py                        2 ✘  pythonProject   at 15:50:08  
  ====================================================================== test session starts ======================================================================
  platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python
  cachedir: .pytest_cache
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  configfile: pytest.ini
  plugins: bdd-8.1.0
  collected 2 items                                                                                                                                               
  
  test_bddParamaterize.py::test_check_varities_of_fruit Fruits: {'apple', 'grapes', 'strawberry'}. There are total of 3
  
  Adding a fruit that is already there in the set.
  There are still 3 fruit varieties.
  
  Tomato added to fruits
  
  There are 4 varieties of fruits.
  PASSED
  test_bddParamaterize.py::test_paramaterize_benefits 
  We have eaten 3 fruits.
  
  We have eaten 2 fruits.
  
  We have 0 fruits remaining.
  PASSED
  
  ======================================================================= 2 passed in 0.01s =======================================================================
  ```

## Pytest-BDD: Scenario Outline

- The `Scenario Outline` keyword can be used to run the same scenario multiple times, with different combination of 
  values. The keyword `Scenario Template` is a synonym of the keyword `Scenario Outline`.
- Copying and Pasting scenarios to use different values quickly becomes tedious and repetitive.

  `exmaple.feature`
  
  ```feature
    Scenario: Paramaterize benefits
      Given We have 5 fruits
      When I eat 3 fruits
      And I eat 2 fruits
      Then I should have 0 fruits
      
    Scenario: Paramaterize benefits
      Given We have 4 fruits
      When I eat 2 fruits
      And I eat 2 fruits
      Then I should have 0 fruits
  ```
  
- We can collapse the 2 similar scenarios into a `Scenario Outline`. We can do it in this fashion.

  `scenarioOutline.feature`
  
  ```feature
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
  ```
  
- Now, we can use the same code that we wrote previously now:

  `test_scenarioOutline.py`
  
  ```python
  from pytest_bdd import scenario, scenarios, when, then, given, parsers
  from pathlib import Path
  import pytest
  from pytest_bdd.generation import print_missing_code
  
  featureFileDir = 'feature_dir'
  featureFile = 'scenarioOutline.feature'
  
  BASE_DIR = Path(__file__).resolve().parent
  FEATURE_FILE=BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)
  
  scenarios(FEATURE_FILE)
  
  @given(parsers.parse("We have {count:d} fruits"),target_fixture="start_fruits")
  def exsistingFruits(count):
      return dict(start=count,eat = 0)
  
  @when(parsers.parse("I eat {eat:d} fruits"))
  def eat3ruits(start_fruits,eat):
      print(f"\nWe have eaten {eat} fruits.")
      start_fruits["eat"] += eat
  
  @then(parsers.parse("I should have {left:d} fruits"))
  def shouldHaveFruits(start_fruits,left):
      diff = start_fruits["start"] - start_fruits["eat"]
      print(f"\nWe have {diff} fruits remaining.")
      assert start_fruits["start"] - start_fruits["eat"] == left
  
  ```
  
- When you execute this, you get the follwing output, and you can see the BDD Test Cases being executed for multiple 
  inputs.

  ```bash
  $  pytest -v -s test_scenarioOutline.py                          ✔  pythonProject   at 15:51:19  
  ====================================================================== test session starts ======================================================================
  platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python
  cachedir: .pytest_cache
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  configfile: pytest.ini
  plugins: bdd-8.1.0
  collected 3 items                                                                                                                                               
  
  test_scenarioOutline.py::test_eating_multiple_fruits_in_sequence[5-3-2-0] 
  We have eaten 3 fruits.
  
  We have eaten 2 fruits.
  
  We have 0 fruits remaining.
  PASSED
  test_scenarioOutline.py::test_eating_multiple_fruits_in_sequence[4-2-2-0] 
  We have eaten 2 fruits.
  
  We have eaten 2 fruits.
  
  We have 0 fruits remaining.
  PASSED
  test_scenarioOutline.py::test_eating_multiple_fruits_in_sequence[10-4-3-3] 
  We have eaten 4 fruits.
  
  We have eaten 3 fruits.
  
  We have 3 fruits remaining.
  PASSED
  
  ======================================================================= 3 passed in 0.01s =======================================================================
  ```