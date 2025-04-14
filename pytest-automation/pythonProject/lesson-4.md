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

    ```bash
	pytest -v test_paramaterize.py                                                   1 ✘  at 20:58:38  
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

  ```bash
   pytest -v test_paramaterize.py                                               ✔  took 3s   at 21:16:31  
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
  
