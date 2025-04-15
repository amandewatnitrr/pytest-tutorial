# Pytest: Paramaterized Tests

## `@pytest.mark.parametrize`

- Paramaterized Test are helpful when we want to do data driven tests, and this can help us in increasing the test coverage.
- Let's say a scenartio when you want to try out our login page with various combinations of username and password. So, we could not be writting the same test again and again for each credential. Rather, we can have them as a key-value pair in a dictionary, and call the same function repeateadly.

- Let's try to understand this through an example:

  `test_paramaterize.py`
  
    ```python
    import pytest	
	dataset = [(1,2),(3,4),(5,6),(7,8),(10,9)]

	class TestCase:
	
	    @pytest.mark.parametrize("a,b", dataset)
	    def test_greater(self, a, b):
	        assert b > a, f"{b} is not greater than {a}"
	
	    def run_tests(self):
	        for a,b in dataset:
	            print(f"Running for a={a} and b={b}")
	            self.test_greater(a,b)
	
	if __name__ == '__main__':
	    test = TestCase()
	    test.run_tests()
   ```
  
- Once you execute the test cases you see something like this:

  <details>
  <summary><b>Output</b></summary>
  
    ```bash
	 $ pytest -v test_paramaterize.py                                                   1 ✘  at 20:58:38  
	============================================================================ test session starts ============================================================================
	platform darwin -- Python 3.11.3, pytest-7.4.2, pluggy-1.3.0 -- /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
	cachedir: .pytest_cache
	rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
	configfile: pytest.ini
	plugins: django-4.5.2
	collected 5 items                                                                                                                                                           
	
	test_paramaterize.py::TestCase::test_greater[1-2] PASSED                                                                                                              [ 20%]
	test_paramaterize.py::TestCase::test_greater[3-4] PASSED                                                                                                              [ 40%]
	test_paramaterize.py::TestCase::test_greater[5-6] PASSED                                                                                                              [ 60%]
	test_paramaterize.py::TestCase::test_greater[7-8] PASSED                                                                                                              [ 80%]
	test_paramaterize.py::TestCase::test_greater[10-9] FAILED                                                                                                             [100%]
	
	================================================================================= FAILURES ==================================================================================
	________________________________________________________________________ TestCase.test_greater[10-9] ________________________________________________________________________
	
	self = <test_paramaterize.TestCase object at 0x103f0d650>, a = 10, b = 9
	
	    @pytest.mark.parametrize("a,b", dataset)
	    def test_greater(self, a, b):
	>       assert b > a, f"{b} is not greater than {a}"
	E       AssertionError: 9 is not greater than 10
	E       assert 9 > 10
	
	test_paramaterize.py:9: AssertionError
	========================================================================== short test summary info ==========================================================================
	FAILED test_paramaterize.py::TestCase::test_greater[10-9] - AssertionError: 9 is not greater than 10
	======================================================================== 1 failed, 4 passed in 0.04s ========================================================================
    ```
  </details>

- Here, it clearly says that 4 tests have passed while 1 failed. Even though we just have one test case written, but is being called for each input individually. As, the parameters are being initialized everytime with the new set.
- Let's see this another example to see how powerful parameterization is:

  ```python
  import pytest
  import math
  
  dataset = [
      ((1,2,3), 'sum', 6),
      ((2,3,4), 'sum', 9),
      ((2,3,4), 'prod', 24)
  ]
  
  dataset1 = [(1,2),(3,4),(5,6),(7,8),(10,9)]
  
  
  class TestCase:
  
      @pytest.mark.parametrize("a,b", dataset1)
      def test_greater(self, a, b):
          assert b > a, f"{b} is not greater than {a}"
  
      @pytest.mark.parametrize("a,b,c",dataset)
      def test_solutions(self,a,b,c):
          try:
              if b == "sum":
                  assert sum(a) == c
              elif b == "prod":
                  assert math.prod(a) == c
          except Exception as e:
              print("Wrong Operation Value Assigned")
  
      def run_tests(self):
          try:
              for a,b,c in dataset:
                  self.test_solutions(a,b,c)
          except Exception as e:
              print("Unknown Error Occurred.")
  
  
  if __name__ == '__main__':
      test = TestCase()
      test.run_tests()
  ```

- Here in this case, as you can clearly see that we have clearly created a complex scenario for explaining the parameterization.
- When you execute this, it will collect 2 test cases and, this 2 test cases will have a total of 8 inputs coming to them. So, 8 tests will be performed and, out of which 7 will pass and, 1 fails.
- Below, is the output of the execution shared:

  <details>
  <summary><b>Output</b></summary>
  
  ```bash
  $ pytest -v test_paramaterize.py                                               ✔  took 3s   at 21:16:31  
  ============================================================================ test session starts ============================================================================
  platform darwin -- Python 3.11.3, pytest-7.4.2, pluggy-1.3.0 -- /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
  cachedir: .pytest_cache
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  configfile: pytest.ini
  plugins: django-4.5.2
  collected 8 items                                                                                                                                                           
  
  test_paramaterize.py::TestCase::test_greater[1-2] PASSED                                                                                                              [ 12%]
  test_paramaterize.py::TestCase::test_greater[3-4] PASSED                                                                                                              [ 25%]
  test_paramaterize.py::TestCase::test_greater[5-6] PASSED                                                                                                              [ 37%]
  test_paramaterize.py::TestCase::test_greater[7-8] PASSED                                                                                                              [ 50%]
  test_paramaterize.py::TestCase::test_greater[10-9] FAILED                                                                                                             [ 62%]
  test_paramaterize.py::TestCase::test_solutions[a0-sum-6] PASSED                                                                                                       [ 75%]
  test_paramaterize.py::TestCase::test_solutions[a1-sum-9] PASSED                                                                                                       [ 87%]
  test_paramaterize.py::TestCase::test_solutions[a2-prod-24] PASSED                                                                                                     [100%]
  
  ================================================================================= FAILURES ==================================================================================
  ________________________________________________________________________ TestCase.test_greater[10-9] ________________________________________________________________________
  
  self = <test_paramaterize.TestCase object at 0x10440e990>, a = 10, b = 9
  
      @pytest.mark.parametrize("a,b", dataset1)
      def test_greater(self, a, b):
  >       assert b > a, f"{b} is not greater than {a}"
  E       AssertionError: 9 is not greater than 10
  E       assert 9 > 10
  
  test_paramaterize.py:17: AssertionError
  ========================================================================== short test summary info ==========================================================================
  FAILED test_paramaterize.py::TestCase::test_greater[10-9] - AssertionError: 9 is not greater than 10
  ======================================================================== 1 failed, 7 passed in 0.05s ========================================================================
  ```
  </details>
  
## Fixtures in Pytest

- This is a mechanism pytest provides us to get ready for the actual tests and, cleanup post the tests are performed. 
- `Fixtures` are functions that are run by pytest before(and sometimes after) the actual test functions. Examples: Setting up a Database Connection, Initialize Web Driver.
- We can put fixtures in individual test files or modules, or we can have it in a directory as well in a `conftest.py` file for making fixtures available in multiple test files.
- We can also return data from fixture functions.
- Fixtures are mainly used to Initialize Connections, Open files etc.
- Let's start learning about this with an example:

  ```python
  import pytest
  
  class TestCases:
  
      @pytest.fixture()
      def setup_city(self):
          print("Fixture under execution.")
          city = ['Singapore','Delhi','Chicago','Almaty']
          return city # It's not mandatory, that a fixture must always return something.
  
      def test_city(self, setup_city):
          try:
              print(setup_city)
              assert setup_city[0]  == 'Singapore'
              assert setup_city[::2] == ['Singapore', 'Chicago']
  
          except Exception as e:
              print(f"Unknown Error Occured {e}")
  
  
  if __name__ == '__main__':
      test = TestCases()
      test.test_city()
  ```

- If you see the debug logs carefully you can see that the fixtures has initialised everything for us already, and the values are directly being used by the testcases.

  <details>
  <summary><b>Output</b></summary>
  
  ```bash
  /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python -X pycache_prefix=/Users/akd/Library/Caches/JetBrains/PyCharmCE2024.2/cpython-cache /Users/akd/Applications/PyCharm Community Edition.app/Contents/plugins/python-ce/helpers/pydev/pydevd.py --multiprocess --qt-support=auto --client 127.0.0.1 --port 49537 --file /Users/akd/Applications/PyCharm Community Edition.app/Contents/plugins/python-ce/helpers/pycharm/_jb_pytest_runner.py --path /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/pytest-topics/test_fixtures.py 
  Testing started at 12:05 pm ...
  Connected to pydev debugger (build 242.23726.102)
  Launching pytest with arguments /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/pytest-topics/test_fixtures.py --no-header --no-summary -q in /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/pytest-topics
  
  ============================= test session starts ==============================
  collecting ... collected 1 item
  
  test_fixtures.py::TestCases::test_city Fixture under execution.
  PASSED                            [100%]['Singapore', 'Delhi', 'Chicago', 'Almaty']
  
  
  ============================== 1 passed in 0.02s ===============================
  
  Process finished with exit code 0
  ```
  </details>

- Also, note that this time the fixture is called by our test function, and then used the return value from the function.
- Let's try something different, let's say we have used fixtures, and we want to use the value of these fizxtures while they are being manipulated before assertion happens. Let's try to understand this with example below:

  ```python
  import pytest
  
  class TestCases:
  
      @pytest.fixture()
      def setup_city(self):
          print("Fixture under execution.")
          city = ['Singapore','Delhi','Chicago','Almaty']
          return city # It's not mandatory, that a fixture must always return something.
  
      def test_city(self, setup_city):
          try:
              print(setup_city)
              assert setup_city[0]  == 'Singapore'
              assert setup_city[::2] == ['Singapore', 'Chicago']
  
          except Exception as e:
              print(f"Unknown Error Occured {e}")
  
      def reverse_str_array(self, lst):
          lst.reverse()
          return lst
  
      def test_city_reversed(self,setup_city):
          try:
              r =  self.reverse_str_array(setup_city)
              print(f"\nReversed Values for the setup_city: {r}")
              assert setup_city[::-1] == self.reverse_str_array(setup_city)
          except Exception as e:
              print(f"Unknown Error Occured {e}")
  
  
  
  if __name__ == '__main__':
      test = TestCases()
      test.test_city()
  ```
  
- Now, when we debug this, this is what we see:

  <details>
  <summary><b>Output</b></summary>
  
  ```bash
  /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python -X pycache_prefix=/Users/akd/Library/Caches/JetBrains/PyCharmCE2024.2/cpython-cache /Users/akd/Applications/PyCharm Community Edition.app/Contents/plugins/python-ce/helpers/pydev/pydevd.py --multiprocess --qt-support=auto --client 127.0.0.1 --port 49662 --file /Users/akd/Applications/PyCharm Community Edition.app/Contents/plugins/python-ce/helpers/pycharm/_jb_pytest_runner.py --path /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/pytest-topics/test_fixtures.py 
  Testing started at 1:13 pm ...
  Connected to pydev debugger (build 242.23726.102)
  Launching pytest with arguments /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/pytest-topics/test_fixtures.py --no-header --no-summary -q in /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/pytest-topics
  
  ============================= test session starts ==============================
  collecting ... collected 2 items
  
  test_fixtures.py::TestCases::test_city Fixture under execution.
  PASSED                            [ 50%]['Singapore', 'Delhi', 'Chicago', 'Almaty']
  
  test_fixtures.py::TestCases::test_city_reversed Fixture under execution.
  PASSED                   [100%]
  Reversed Values for the setup_city: ['Almaty', 'Chicago', 'Delhi', 'Singapore']
  
  
  ============================== 2 passed in 0.02s ===============================
  
  Process finished with exit code 0
  ```
  </details>

### Implementing Fixtures using Decorators

- We can also call the fixtures using markers as well. We can call a fixture using the decorator.
  
  ```python
  @pytest.mark.usefixtures("fixture_name")
  ```

- Let's see this through an example again over here:

  ```python
  import pytest
  
  class TestCases:
  
      @pytest.fixture()
      def setup_city(self):
          print("Fixture under execution.")
          city = ['Singapore','Delhi','Chicago','Almaty']
          return city # It's not mandatory, that a fixture must always return something.
  
      def test_city(self, setup_city):
          try:
              print(setup_city)
              assert setup_city[0]  == 'Singapore'
              assert setup_city[::2] == ['Singapore', 'Chicago']
  
          except Exception as e:
              print(f"Unknown Error Occured {e}")
  
      def reverse_str_array(self, lst):
          lst.reverse()
          return lst
  
      def test_city_reversed(self,setup_city):
          try:
              r =  self.reverse_str_array(setup_city)
              print(f"\nReversed Values for the setup_city: {r}")
              assert setup_city[::-1] == self.reverse_str_array(setup_city)
          except Exception as e:
              print(f"Unknown Error Occured {e}")
  
      @pytest.mark.usefixtures("setup_city")
      def test_alwaysTure(self):
          assert 1==1
  
  
  
  if __name__ == '__main__':
      test = TestCases()
  ```

- If you look atn the output for this, we see the following:

  <details>
  <summary><b>Output</b></summary>
  
  ```bash
  $ pytest -v -s test_fixtures.py                                        4 ✘  pythonProject   at 13:34:15  
  ============================================================================ test session starts ============================================================================
  platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python
  cachedir: .pytest_cache
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  configfile: pytest.ini
  collected 3 items                                                                                                                                                           
  
  test_fixtures.py::TestCases::test_city Fixture under execution.
  ['Singapore', 'Delhi', 'Chicago', 'Almaty']
  PASSED
  test_fixtures.py::TestCases::test_city_reversed Fixture under execution.
  
  Reversed Values for the setup_city: ['Almaty', 'Chicago', 'Delhi', 'Singapore']
  PASSED
  test_fixtures.py::TestCases::test_alwaysTure Fixture under execution.
  PASSED
  
  ============================================================================= 3 passed in 0.00s =============================================================================
  ```
  </details>

- The fixture was also called for the test `test_alwaysTrue` by the marker and, not by the function.
- But, the problem in this scenario is we cannot use the return value from the fixture when called using marker or decorator.
- You can see this clearly in the example below:

  ```python
  import pytest
  
  class TestCases:
  
      @pytest.fixture()
      def setup_city(self):
          print("Fixture under execution.")
          city = ['Singapore','Delhi','Chicago','Almaty']
          return city # It's not mandatory, that a fixture must always return something.
  
      def test_city(self, setup_city):
          try:
              print(setup_city)
              assert setup_city[0]  == 'Singapore'
              assert setup_city[::2] == ['Singapore', 'Chicago']
  
          except Exception as e:
              print(f"Unknown Error Occured {e}")
  
      def reverse_str_array(self, lst):
          lst.reverse()
          return lst
  
      def test_city_reversed(self,setup_city):
          try:
              r =  self.reverse_str_array(setup_city)
              print(f"\nReversed Values for the setup_city: {r}")
              assert setup_city[::-1] == self.reverse_str_array(setup_city)
          except Exception as e:
              print(f"Unknown Error Occured {e}")
  
  
      @pytest.mark.usefixtures("setup_city")
      def test_alwaysTure(self):
          assert 1==1
  
      @pytest.mark.xfail(reason="usefixture decorator cannot use the return value coming from the Fixture.")
      @pytest.mark.usefixtures("setup_city")
      def test_fixtureAccessUsingMark(self):
          assert setup_city[0] == 'Singapore'
  
  
  if __name__ == '__main__':
      test = TestCases()
  ```

- Here, in the output below you can clearly see that, we are inside the fixture, as the statement prints `Fixture under execution`. But, when tried to access it's value, it says undefined.
  
  <details>
  <summary><b>Output</b></summary>
  
  ```bash
  Fixture under execution.
  XFAILthe
  Fixture.)                                                                [100%]
  self = <test_fixtures.TestCases object at 0x104863a50>
  
      @pytest.mark.xfail(reason="usefixture decorator cannot use the return value coming from the Fixture.")
      @pytest.mark.usefixtures("setup_city")
      def test_fixtureAccessUsingMark(self):
  >       assert setup_city[0] == 'Singapore'
  E       NameError: name 'setup_city' is not defined
  
  test_fixtures.py:40: NameError
  ```
  </details>
  
### Setup/Teardown in Fixtures

- We can also use fixtures to perform setup and teardown operations. We can use `yield` keyword to perform the teardown operations.
- In order to mark a function as fiture use the decorator:

  ```python
  @pytest.fixture()
  ```
- Let's try to understand this through an example:

  ```python
  import pytest
  
  days_1 = ['mon', 'tue', 'wed']
  days_2 = ['fri', 'sat', 'sun']
  
  class TestCases:
  
      @pytest.fixture()
      def setup_city(self):
          print("Fixture under execution.")
          city = ['Singapore','Delhi','Chicago','Almaty']
          return city # It's not mandatory, that a fixture must always return something.
  
      def test_city(self, setup_city):
          try:
              print(setup_city)
              assert setup_city[0]  == 'Singapore'
              assert setup_city[::2] == ['Singapore', 'Chicago']
  
          except Exception as e:
              print(f"Unknown Error Occured {e}")
  
      def reverse_str_array(self, lst):
          lst.reverse()
          return lst
  
      def test_city_reversed(self,setup_city):
          try:
              r =  self.reverse_str_array(setup_city)
              print(f"\nReversed Values for the setup_city: {r}")
              assert setup_city[::-1] == self.reverse_str_array(setup_city)
          except Exception as e:
              print(f"Unknown Error Occured {e}")
  
  
      @pytest.mark.usefixtures("setup_city")
      def test_alwaysTure(self):
          assert 1==1
  
      @pytest.mark.xfail(reason="usefixture decorator cannot use the return value coming from the Fixture.")
      @pytest.mark.usefixtures("setup_city")
      def test_fixtureAccessUsingMark(self):
          assert setup_city[0] == 'Singapore'
  
      @pytest.fixture()
      def teardown_setup(self):
          wk = days_1.copy()
          wk.append('thur')
          yield wk
  
          # Teardown started
          print("\n Week Completed - Teardown Started")
          wk.pop()
          print("Teardown Ended")
  
      def test_completeWeek(self, teardown_setup):
          teardown_setup.extend(days_2)
          try:
              assert teardown_setup == ['mon', 'tue', 'wed', 'thur','fri', 'sat', 'sun']
          except Exception as e:
              print(f"Error Occured: {e}.")
  
  
  if __name__ == '__main__':
      test = TestCases()
  ```
  
- In the above example, where we have specified `teardown_setup()` as a fixture using the decorator `@pytest.fixture()`.
- Everything above and including the `yield` statement is the setup, while everything following it is part of teardown.
- Once you execute this, you will see the following output:

  <details>
  <summary><b>Output</b></summary>
  
  ```bash
  $ pytest -v -s test_fixtures.py                                          ✔  pythonProject   at 16:36:14  
  ============================================================================ test session starts ============================================================================
  platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python
  cachedir: .pytest_cache
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  configfile: pytest.ini
  collected 5 items                                                                                                                                                           
  
  test_fixtures.py::TestCases::test_city Fixture under execution.
  ['Singapore', 'Delhi', 'Chicago', 'Almaty']
  PASSED
  test_fixtures.py::TestCases::test_city_reversed Fixture under execution.
  
  Reversed Values for the setup_city: ['Almaty', 'Chicago', 'Delhi', 'Singapore']
  PASSED
  test_fixtures.py::TestCases::test_alwaysTure Fixture under execution.
  PASSED
  test_fixtures.py::TestCases::test_fixtureAccessUsingMark Fixture under execution.
  XFAIL (usefixture decorator cannot use the return value coming from the Fixture.)
  test_fixtures.py::TestCases::test_completeWeek PASSED
   Week Completed - Teardown Started
  Teardown Ended
  ======================================================================= 4 passed, 1 xfailed in 0.02s ========================================================================
  ```
  </details>
  
### Multiple Fixtures

- We can have multiple fixtures within the same program as well, let's see this through an example:

  ```python
  import pytest
  
  days_1 = ['mon', 'tue', 'wed']
  days_2 = ['fri', 'sat', 'sun']
  
  class TestCases:
  
      @pytest.fixture()
      def setup_city(self):
          print("Fixture under execution.")
          city = ['Singapore','Delhi','Chicago','Almaty']
          return city # It's not mandatory, that a fixture must always return something.
  
      def test_city(self, setup_city):
          try:
              print(setup_city)
              assert setup_city[0]  == 'Singapore'
              assert setup_city[::2] == ['Singapore', 'Chicago']
  
          except Exception as e:
              print(f"Unknown Error Occured {e}")
  
      def reverse_str_array(self, lst):
          lst.reverse()
          return lst
  
      def test_city_reversed(self,setup_city):
          try:
              r =  self.reverse_str_array(setup_city)
              print(f"\nReversed Values for the setup_city: {r}")
              assert setup_city[::-1] == self.reverse_str_array(setup_city)
          except Exception as e:
              print(f"Unknown Error Occured {e}")
  
  
      @pytest.mark.usefixtures("setup_city")
      def test_alwaysTure(self):
          assert 1==1
  
      @pytest.mark.xfail(reason="usefixture decorator cannot use the return value coming from the Fixture.")
      @pytest.mark.usefixtures("setup_city")
      def test_fixtureAccessUsingMark(self):
          assert setup_city[0] == 'Singapore'
  
      @pytest.fixture()
      def teardown_setup(self):
          wk = days_1.copy()
          wk.append('thur')
          yield wk
  
          # Teardown started
          print("\n Week Completed - Teardown Started")
          wk.pop()
          print("Teardown Ended")
  
      def test_completeWeek(self, teardown_setup):
          teardown_setup.extend(days_2)
          try:
              assert teardown_setup == ['mon', 'tue', 'wed', 'thur','fri', 'sat', 'sun']
          except Exception as e:
              print(f"Error Occured: {e}.")
  
      @pytest.fixture()
      def days_2_manipulation(self):
          wk = days_2.copy()
          wk.insert(0,'thur')
          yield wk
          print("days_2 manipulation over.")
  
      def test_equalLength(self,teardown_setup,days_2_manipulation):
          try:
              assert len(days_1 + days_2_manipulation) == len(teardown_setup + days_2)
          except Exception as e:
              print(f"Unexpected Error Occurred: {e}")
  
  
  if __name__ == '__main__':
      test = TestCases()
  ```

- Once executed, you get the following output:

  <details>
  <summary><b>Output</b></summary>
  
  ```bash
  $ pytest -v -s test_fixtures.py                                      127 ✘  pythonProject   at 16:52:33  
  ============================================================================ test session starts ============================================================================
  platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python
  cachedir: .pytest_cache
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  configfile: pytest.ini
  collected 6 items                                                                                                                                                           
  
  test_fixtures.py::TestCases::test_city Fixture under execution.
  ['Singapore', 'Delhi', 'Chicago', 'Almaty']
  PASSED
  test_fixtures.py::TestCases::test_city_reversed Fixture under execution.
  
  Reversed Values for the setup_city: ['Almaty', 'Chicago', 'Delhi', 'Singapore']
  PASSED
  test_fixtures.py::TestCases::test_alwaysTure Fixture under execution.
  PASSED
  test_fixtures.py::TestCases::test_fixtureAccessUsingMark Fixture under execution.
  XFAIL (usefixture decorator cannot use the return value coming from the Fixture.)
  test_fixtures.py::TestCases::test_completeWeek PASSED
   Week Completed - Teardown Started
  Teardown Ended
  
  test_fixtures.py::TestCases::test_equalLength PASSEDdays_2 manipulation over.
  
  Week Completed - Teardown Started
  Teardown Ended
  ======================================================================= 5 passed, 1 xfailed in 0.01s ========================================================================
  ```
  </details>
  
### Teardown Example for File Operations

- Here's a great example for file operations:

  ```python
  import pytest
  import os
  
  days_1 = ['mon', 'tue', 'wed']
  days_2 = ['fri', 'sat', 'sun']
  filename = "file1.txt"
  
  class TestCases:
  
      @pytest.fixture()
      def setup_city(self):
          print("Fixture under execution.")
          city = ['Singapore','Delhi','Chicago','Almaty']
          return city # It's not mandatory, that a fixture must always return something.
  
      def test_city(self, setup_city):
          try:
              print(setup_city)
              assert setup_city[0]  == 'Singapore'
              assert setup_city[::2] == ['Singapore', 'Chicago']
  
          except Exception as e:
              print(f"Unknown Error Occured {e}")
  
      def reverse_str_array(self, lst):
          lst.reverse()
          return lst
  
      def test_city_reversed(self,setup_city):
          try:
              r =  self.reverse_str_array(setup_city)
              print(f"\nReversed Values for the setup_city: {r}")
              assert setup_city[::-1] == self.reverse_str_array(setup_city)
          except Exception as e:
              print(f"Unknown Error Occured {e}")
  
  
      @pytest.mark.usefixtures("setup_city")
      def test_alwaysTure(self):
          assert 1==1
  
      @pytest.mark.xfail(reason="usefixture decorator cannot use the return value coming from the Fixture.")
      @pytest.mark.usefixtures("setup_city")
      def test_fixtureAccessUsingMark(self):
          assert setup_city[0] == 'Singapore'
  
      @pytest.fixture()
      def teardown_setup(self):
          wk = days_1.copy()
          wk.append('thur')
          yield wk
  
          # Teardown started
          print("\n Week Completed - Teardown Started")
          wk.pop()
          print("Teardown Ended")
  
      def test_completeWeek(self, teardown_setup):
          teardown_setup.extend(days_2)
          try:
              assert teardown_setup == ['mon', 'tue', 'wed', 'thur','fri', 'sat', 'sun']
          except Exception as e:
              print(f"Error Occured: {e}.")
  
      @pytest.fixture()
      def days_2_manipulation(self):
          wk = days_2.copy()
          wk.insert(0,'thur')
          yield wk
          print("days_2 manipulation over.")
  
      def test_equalLength(self,teardown_setup,days_2_manipulation):
          try:
              assert len(days_1 + days_2_manipulation) == len(teardown_setup + days_2)
          except Exception as e:
              print(f"Unexpected Error Occurred: {e}")
  
      @pytest.fixture()
      def file_write(self):
          f = open(filename, 'w')
          print("File Written with Data.")
          f.write("Pytest is good.")
          f.close()
          f = open(filename, 'r+')
          yield f
          print("\n File Available for reading")
          f.close()
          os.remove(filename)
          print("\n File is deleted after, test execution.")
  
      def test_fileData(self, file_write):
          try:
              assert (file_write.readline()) == "Pytest is good."
          except Exception as e:
              print(f"Unknown error occured {e}.")
  
  
  if __name__ == '__main__':
      test = TestCases()
  ```

- Below is the output:

  <details>
  <summary><b>Output</b></summary>
  
  ```bash
  $  pytest -v -s test_fixtures.py                                                             ✔  at 18:13:44  
  ============================================================================ test session starts =============================================================================
  platform darwin -- Python 3.11.3, pytest-7.4.2, pluggy-1.3.0 -- /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
  cachedir: .pytest_cache
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  configfile: pytest.ini
  plugins: django-4.5.2
  collected 7 items                                                                                                                                                            
  
  test_fixtures.py::TestCases::test_city Fixture under execution.
  ['Singapore', 'Delhi', 'Chicago', 'Almaty']
  PASSED
  test_fixtures.py::TestCases::test_city_reversed Fixture under execution.
  
  Reversed Values for the setup_city: ['Almaty', 'Chicago', 'Delhi', 'Singapore']
  PASSED
  test_fixtures.py::TestCases::test_alwaysTure Fixture under execution.
  PASSED
  test_fixtures.py::TestCases::test_fixtureAccessUsingMark Fixture under execution.
  XFAIL (usefixture decorator cannot use the return value coming from the Fixture.)
  test_fixtures.py::TestCases::test_completeWeek PASSED
   Week Completed - Teardown Started
  Teardown Ended
  
  test_fixtures.py::TestCases::test_equalLength PASSEDdays_2 manipulation over.
  
   Week Completed - Teardown Started
  Teardown Ended
  
  test_fixtures.py::TestCases::test_fileData File Written with Data.
  PASSED
   File Available for reading
  
   File is deleted after, test execution.
  ======================================================================== 6 passed, 1 xfailed in 0.02s ========================================================================
  ```
  </details>


### Pytest: Sharing Fixtures

- If we want too make fixtures available in one file, to fixtures in another file, we will have to use plugin called `conftest.py` file.
> [!IMPORTANT]
> `conftest.py` file is a python module, the fixtures written in that file are available throughout the directory, as well anywhere within the sub-directory within the directory it exsists. 
> We can have multiple `conftest.py` file in multiple subdirectories, but only 1 in each of them.

> [!TIP]
> `conftest.py` should not be imported by test files as it is a python module. 
> The `conftest.py` is automatically identified by the pytest during the test execution.

- Let's look at an example of how we can use the `conftest.py` file:

  `conftest.py` file

  ```python
  import pytest
  import os
  
  def pytest_configure():
      pytest.days_1 = ['mon', 'tue', 'wed']
      pytest.days_2 = ['fri', 'sat', 'sun']
  
  
  @pytest.fixture()
  def setup_city():
      print("Fixture under execution.")
      city = ['Singapore','Delhi','Chicago','Almaty']
      return city
  
  @pytest.fixture()
  def file_write():
      pytest.filename = "file1.txt"
      f = open(pytest.filename, 'w')
      print("File Written with Data.")
      f.write("Pytest is good.")
      f.close()
      f = open(pytest.filename, 'r+')
      yield f
      print("\n File Available for reading")
      f.close()
      os.remove(pytest.filename)
      print("\n File is deleted after, test execution.")
  ```

  `test_fixture.py`

  ```python
  import pytest
  import os
  
  class TestCases:
  
      def test_city(self, setup_city):
          try:
              print(setup_city)
              assert setup_city[0]  == 'Singapore'
              assert setup_city[::2] == ['Singapore', 'Chicago']
  
          except Exception as e:
              print(f"Unknown Error Occured {e}")
  
      def reverse_str_array(self, lst):
          lst.reverse()
          return lst
  
      def test_city_reversed(self,setup_city):
          try:
              r =  self.reverse_str_array(setup_city)
              print(f"\nReversed Values for the setup_city: {r}")
              assert setup_city[::-1] == self.reverse_str_array(setup_city)
          except Exception as e:
              print(f"Unknown Error Occured {e}")
  
  
      @pytest.mark.usefixtures("setup_city")
      def test_alwaysTure(self):
          assert 1==1
  
      @pytest.mark.xfail(reason="usefixture decorator cannot use the return value coming from the Fixture.")
      @pytest.mark.usefixtures("setup_city")
      def test_fixtureAccessUsingMark(self):
          assert setup_city[0] == 'Singapore'
  
      @pytest.fixture()
      def teardown_setup(self):
          wk = pytest.days_1.copy()
          wk.append('thur')
          yield wk
  
          # Teardown started
          print("\n Week Completed - Teardown Started")
          wk.pop()
          print("Teardown Ended")
  
      def test_completeWeek(self, teardown_setup):
          teardown_setup.extend(pytest.days_2)
          try:
              assert teardown_setup == ['mon', 'tue', 'wed', 'thur','fri', 'sat', 'sun']
          except Exception as e:
              print(f"Error Occured: {e}.")
  
      @pytest.fixture()
      def days_2_manipulation(self):
          wk = pytest.days_2.copy()
          wk.insert(0,'thur')
          yield wk
          print("days_2 manipulation over.")
  
      def test_equalLength(self,teardown_setup,days_2_manipulation):
          try:
              assert len(pytest.days_1 + days_2_manipulation) == len(teardown_setup + pytest.days_2)
          except Exception as e:
              print(f"Unexpected Error Occurred: {e}")
  
      def test_fileData(self, file_write):
          try:
              assert (file_write.readline()) == "Pytest is good."
          except Exception as e:
              print(f"Unknown error occured {e}.")
  
  
  if __name__ == '__main__':
      test = TestCases()
  ```

- As, we can see we have shifted various fixtures to the `conftest.py` file, and if you run this with the changes done, it still executes successfully as expected the same way. Here's the output to the same:

  <details>
  <summary><b>Output</b></summary>
  
  ```bash
  $ pytest -v -s test_fixtures.py                                                  ✔  at 21:29:47  
  ========================================================================== test session starts ==========================================================================
  platform darwin -- Python 3.11.3, pytest-7.4.2, pluggy-1.3.0 -- /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
  cachedir: .pytest_cache
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  configfile: pytest.ini
  plugins: django-4.5.2
  collected 7 items                                                                                                                                                       
  
  test_fixtures.py::TestCases::test_city Fixture under execution.
  ['Singapore', 'Delhi', 'Chicago', 'Almaty']
  PASSED
  test_fixtures.py::TestCases::test_city_reversed Fixture under execution.
  
  Reversed Values for the setup_city: ['Almaty', 'Chicago', 'Delhi', 'Singapore']
  PASSED
  test_fixtures.py::TestCases::test_alwaysTure Fixture under execution.
  PASSED
  test_fixtures.py::TestCases::test_fixtureAccessUsingMark Fixture under execution.
  XFAIL (usefixture decorator cannot use the return value coming from the Fixture.)
  test_fixtures.py::TestCases::test_completeWeek PASSED
   Week Completed - Teardown Started
  Teardown Ended
  
  test_fixtures.py::TestCases::test_equalLength PASSEDdays_2 manipulation over.
  
   Week Completed - Teardown Started
  Teardown Ended
  
  test_fixtures.py::TestCases::test_fileData File Written with Data.
  PASSED
   File Available for reading
  
   File is deleted after, test execution.
  ===================================================================== 6 passed, 1 xfailed in 0.02s ======================================================================
  ```
  </details>

> [!NOTE]
> Fixtures can be overriden from test module level.
> The Fixtures in the subdirectory will override the fixtures coming from the parent direcotry if they have the same name.

> [!NOTE]
> If you want to track the execution of the fixtures use the `--setup-show` option when executing the pytest command.

- Let's trace the fixture execution through the example we just used.

  <details>
  <summary><b>Output</b></summary>
  
  ```bash
  $ pytest -v -s test_fixtures.py --setup-show                                              ✔  at 22:05:05  
  ========================================================================== test session starts ==========================================================================
  platform darwin -- Python 3.11.3, pytest-7.4.2, pluggy-1.3.0 -- /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
  cachedir: .pytest_cache
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  configfile: pytest.ini
  plugins: django-4.5.2
  collected 7 items                                                                                                                                                       
  
  test_fixtures.py::TestCases::test_city 
  SETUP    S _fail_for_invalid_template_variable
  SETUP    S django_test_environment
  SETUP    S django_db_blocker
        SETUP    C _django_setup_unittest (fixtures used: django_db_blocker)
          SETUP    F _dj_autoclear_mailbox
          SETUP    F _django_clear_site_cache
          SETUP    F _django_db_marker
          SETUP    F _django_set_urlconf
          SETUP    F _live_server_helper
          SETUP    F _template_string_if_invalid_markerFixture under execution.
  
          SETUP    F setup_city
          pytest-topics/test_fixtures.py::TestCases::test_city (fixtures used: _dj_autoclear_mailbox, _django_clear_site_cache, _django_db_marker, _django_set_urlconf, _django_setup_unittest, _fail_for_invalid_template_variable, _live_server_helper, _template_string_if_invalid_marker, django_db_blocker, django_test_environment, request, setup_city)['Singapore', 'Delhi', 'Chicago', 'Almaty']
  PASSED
          TEARDOWN F setup_city
          TEARDOWN F _template_string_if_invalid_marker
          TEARDOWN F _live_server_helper
          TEARDOWN F _django_set_urlconf
          TEARDOWN F _django_db_marker
          TEARDOWN F _django_clear_site_cache
          TEARDOWN F _dj_autoclear_mailbox
  ```
  </details>
  
- This is a small portion of the output that we got, we clearly see here `SETUP F setup_city`, that the setup for fixture has been done.
- On the next line it clearly specifies the following, here at the end you can find `setup_city` in the fixture used list, with it's respective values. Not all the setup mentioned here are not needed.

  ```bash
  pytest-topics/test_fixtures.py::TestCases::test_city (fixtures used: _dj_autoclear_mailbox, _django_clear_site_cache, _django_db_marker, _django_set_urlconf, _django_setup_unittest, _fail_for_invalid_template_variable, _live_server_helper, _template_string_if_invalid_marker, django_db_blocker, django_test_environment, request, setup_city)['Singapore', 'Delhi', 'Chicago', 'Almaty']
  ```
  
### Introspecting the Calling Test Function

> [!IMPORTANT]
> Pytest `request` fixture allows your fixtures to inspect the test functions using them. This is useful for dynamic behaviour based on test properites.

- Let's learn this through an example:

  `test_introspect.py`

  ```python
  import pytest
  
  class Testcases:
  
      def test_addition(self,function_detail):
          assert 1 + 1 == 2
  
  if __name__ == '__main__':
      test = Testcases()
  ```
  
  `conftest.py`

  ```python
  @pytest.fixture()
  def function_detail(request):
      print(f"\nStarting test: {request.node.name}")
      print(f"\nIn Module: {request.module.__name__}")
      print(f"\n Request Scope: {request.scope}")
      yield
      print(f"\nFinished test: {request.node.name}")
  ```
  
- Once, you execute this you see the following output:

  <details>
  <summary><b>Output</b></summary>
  
  ```bash
  $  pytest -v -s test_introspect.py                                          ✔  at 22:50:05  
  ========================================================================== test session starts ==========================================================================
  platform darwin -- Python 3.11.3, pytest-7.4.2, pluggy-1.3.0 -- /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
  cachedir: .pytest_cache
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  configfile: pytest.ini
  plugins: django-4.5.2
  collected 1 item                                                                                                                                                        
  
  test_introspect.py::Testcases::test_addition 
  Starting test: test_addition
  
  In Module: test_introspect
  
   Request Scope: function
  PASSED
  Finished test: test_addition
  =========================================================================== 1 passed in 0.01s ===========================================================================
  ```
  </details>
  
- Here, it clearly shows:
  - `test function name` for `request.node.name`.
  - `test file name` for `request.module.__name__`
  - `scope of the test` for `request.scope`

- `request.function.__name__` is same as `request.node.name`.
- based on this the developer can decide to have a certain logic or c3ertain set of inputs to be given based the function from which the request is coming.
- We can also fetch variable from the module using the following way shown below:

  `conftest.py`

  ```python
  @pytest.fixture()
  def function_detail(request):
      print(f"\nStarting test: {request.node.name}")
      print(f"\nIn Module: {request.module.__name__}")
      print(f"\n Request Scope: {request.scope}")
      print(f"\n Function Name: {request.function.__name__}")
      digits =  getattr(request.module, "digits")
      print(f"\n Digits: {digits}")
      yield
      print(f"\nFinished test: {request.node.name}")
  ```
  
  `test_introspect.py`

  ```python
  import pytest
  
  digits = [1,2,3,4,5,6,7,8,9,0]
  
  class Testcases:
  
      def test_addition(self,function_detail):
          assert 1 + 1 == 2
  
  if __name__ == '__main__':
      test = Testcases()
  ```
  
- Once executed, you will see the following output:

  <details>
  <summary><b>Output</b></summary>
  
  ```bash
  $ pytest -v -s test_introspect.py                                          ✔  at 22:54:57  
  ========================================================================== test session starts ==========================================================================
  platform darwin -- Python 3.11.3, pytest-7.4.2, pluggy-1.3.0 -- /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
  cachedir: .pytest_cache
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  configfile: pytest.ini
  plugins: django-4.5.2
  collected 1 item                                                                                                                                                        
  
  test_introspect.py::Testcases::test_addition 
  Starting test: test_addition
  
  In Module: test_introspect
  
   Request Scope: function
  
   Function Name: test_addition
  
   Digits: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
  PASSED
  Finished test: test_addition  
  =========================================================================== 1 passed in 0.01s ===========================================================================
  ```
  </details>
  

- And, we can also manipulate the data and yield it to return the value for further usage depending upon the needs.

### Factories as Fixtures

- If we want to put some logic into the fixture based on the calling test-function. This is helpful in such scenarios. This is called `Factories as Fixtures`.
- This can help in situations where the result of a fixture is needed multiple times in a single test.
- Instead of returning data directly, the fixture instead returns a function which generates the data. This function can than be called multiple times in the test.
- Let's try some examples:

  `test_introspect.py`
  
  ```python
  import pytest
  
  digits = [1,2,3,4,5,6,7,8,9,0]
  
  class Testcases:
  
      def test_addition(self,function_detail):
          assert 1 + 1 == 2
  
      def test_factory(self,return_tuple_or_list):
          assert type(return_tuple_or_list('tuple')) == tuple
          assert type(return_tuple_or_list('list')) == list
  
  
  if __name__ == '__main__':
      test = Testcases()
  ```
  
  `conftest.py`
  
  ```python
  import pytest
  import os
  
  def pytest_configure():
      pytest.days_1 = ['mon', 'tue', 'wed']
      pytest.days_2 = ['fri', 'sat', 'sun']
  
  
  @pytest.fixture()
  def setup_city():
      print("Fixture under execution.")
      city = ['Singapore','Delhi','Chicago','Almaty']
      return city
  
  @pytest.fixture()
  def file_write():
      pytest.filename = "file1.txt"
      f = open(pytest.filename, 'w')
      print("File Written with Data.")
      f.write("Pytest is good.")
      f.close()
      f = open(pytest.filename, 'r+')
      yield f
      print("\n File Available for reading")
      f.close()
      os.remove(pytest.filename)
      print("\n File is deleted after, test execution.")
  
  
  @pytest.fixture()
  def function_detail(request):
      print(f"\nStarting test: {request.node.name}")
      print(f"\nIn Module: {request.module.__name__}")
      print(f"\n Request Scope: {request.scope}")
      print(f"\n Function Name: {request.function.__name__}")
      digits =  getattr(request.module, "digits")
      print(f"\n Digits: {digits}")
      yield
      print(f"\nFinished test: {request.node.name}")
  
  @pytest.fixture()
  def return_tuple_or_list():
      def get_dt(name):
          if name == 'list':
              return [1,2,3]
          elif name == 'tuple':
              return (1,2,3)
          else:
              raise ValueError("Invalid type requested")
      return get_dt
  ```
  
- Once you execute this, you will see the following output:

  <details>
  <summary><b>Output</b></summary>
  
  ```bash
  $ pytest -v -s test_introspect.py                                              1 ✘  at 23:32:33  
  ========================================================================== test session starts ==========================================================================
  platform darwin -- Python 3.11.3, pytest-7.4.2, pluggy-1.3.0 -- /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
  cachedir: .pytest_cache
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  configfile: pytest.ini
  plugins: django-4.5.2
  collected 2 items                                                                                                                                                       
  
  test_introspect.py::Testcases::test_addition 
  Starting test: test_addition
  
  In Module: test_introspect
  
   Request Scope: function
  
   Function Name: test_addition
  
   Digits: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
  PASSED
  Finished test: test_addition
  
  test_introspect.py::Testcases::test_factory PASSED
  
  =========================================================================== 2 passed in 0.01s ===========================================================================
  ```
  </details>
  
- And, here we see that the `test_factory` test has passed. basically, we created a fixture that returns a complete function in itself, that will return a value, based on the input provided to the fixture.

### Paramatrizing from Fixtures

- Let's start with an example itself. We have create a fixture `return_tuple_list` for test `test_typeIntype.

  `test_introspect.py`

  ```python
  import pytest
  
  digits = [1,2,3,4,5,6,7,8,9,0]
  
  class Testcases:
  
      def test_addition(self,function_detail):
          assert 1 + 1 == 2
  
      def test_factory(self,return_tuple_or_list):
          assert type(return_tuple_or_list('tuple')) == tuple
          assert type(return_tuple_or_list('list')) == list
  
      def test_typeIntype(self,return_tuple_list):
          assert (type(return_tuple_list)) in [tuple,list]
  
  
  if __name__ == '__main__':
      test = Testcases()
  ```
  
  `conftest.py`

  ```python
  import pytest
  import os
  
  def pytest_configure():
      pytest.days_1 = ['mon', 'tue', 'wed']
      pytest.days_2 = ['fri', 'sat', 'sun']
  
  
  @pytest.fixture()
  def setup_city():
      print("Fixture under execution.")
      city = ['Singapore','Delhi','Chicago','Almaty']
      return city
  
  @pytest.fixture()
  def file_write():
      pytest.filename = "file1.txt"
      f = open(pytest.filename, 'w')
      print("File Written with Data.")
      f.write("Pytest is good.")
      f.close()
      f = open(pytest.filename, 'r+')
      yield f
      print("\n File Available for reading")
      f.close()
      os.remove(pytest.filename)
      print("\n File is deleted after, test execution.")
  
  
  @pytest.fixture()
  def function_detail(request):
      print(f"\nStarting test: {request.node.name}")
      print(f"\nIn Module: {request.module.__name__}")
      print(f"\n Request Scope: {request.scope}")
      print(f"\n Function Name: {request.function.__name__}")
      digits =  getattr(request.module, "digits")
      print(f"\n Digits: {digits}")
      yield
      print(f"\nFinished test: {request.node.name}")
  
  @pytest.fixture()
  def return_tuple_or_list():
      def get_dt(name):
          if name == 'list':
              return [1,2,3]
          elif name == 'tuple':
              return (1,2,3)
          else:
              raise ValueError("Invalid type requested")
      return get_dt
  
  @pytest.fixture(params=[(1,2),[3,4]], ids=['tuple', 'list'])
  def return_tuple_list(request):
      return request.param
  ```
  
- The test here will be called twice as it has 2 inputs, and hence it has both the type, as it has a list and a tuple. It will pass both the times. And, when executed the output looks something like this:

  <details>
  <summary><b>Output</b></summary>
  
  ```bash
  pytest -v -s test_introspect.py                                             ✔  at 23:52:56  
  ========================================================================== test session starts ==========================================================================
  platform darwin -- Python 3.11.3, pytest-7.4.2, pluggy-1.3.0 -- /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
  cachedir: .pytest_cache
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  configfile: pytest.ini
  plugins: django-4.5.2
  collected 4 items                                                                                                                                                       
  
  test_introspect.py::Testcases::test_addition 
  Starting test: test_addition
  
  In Module: test_introspect
  
   Request Scope: function
  
   Function Name: test_addition
  
   Digits: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
  PASSED
  Finished test: test_addition
  
  test_introspect.py::Testcases::test_factory PASSED
  test_introspect.py::Testcases::test_typeIntype[tuple] PASSED
  test_introspect.py::Testcases::test_typeIntype[list] PASSED
  
  =========================================================================== 4 passed in 0.01s ===========================================================================
  ```
  </details>
  
### Fixture Scope

- Fixture scope determines how often a fixture is initialized and torn down during a test run. Pytest supports 5 scopes, listed from shortest to longest lifetime:

  - function(default)
  - class
  - module
  - package
  - session

#### Function Scope 

- This is the default scope. The fixture is invoked once per test function.
- It is initialized orr setup before each test function and teardown after the function execution is completed.
- It is used in situations where we need fresh data/state for eevery test.

#### Class Scope

- It initializes once per test class, and teardown happens once all the tests in the class have completed there execution.
- It is used in scenarios where we need shared setup for all methods in a class.

#### Module Scope

- It is initialized once per module, and will teardown only after all the tests in the module have finished there execution.
- It is used in scenarios where initializtion is resource expensive, for example setting up a Database Connection.

#### Session Scope

- Scope  wise this is this has the longest lifeline among all the scopes.
- This is initialized once per test session, and will teardown once all the tests that are supposed to be executed during the session have finished there execution.
- This is used in scenarios where we have Global Configurations that we need to test or cross-test dependencies.

> [!IMPORTANT]
> The Scope Hierarchy is as follows: <br/>
> `session > package > module > class > function` <br/>
> - Higher scoped fixtures are instantiated first. 
> - Fixtures can depend on higher or same scopes but not lower.

> [!TIP]
> Use `narrowest scope` possible for test isolation.
> Use `broader scope` for:
>   - Expensive Resources (example: Database, APIs)
>   - Read-only Configurations
> Avoid `mutable state` in broader scopes.