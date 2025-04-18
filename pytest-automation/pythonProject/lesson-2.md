# Pytest Assertions and Test Discovery

![](./imgs/Getting-Started-with-Testing-in-Python_Watermarked.webp)

## Assertions & Class Based Test Cases


### Assertions

- Assertions are way of validating our tests. They are the main component of the test.
- Unless you validate what you are exepcting, you can't be sure if your test is passing or failing.
- The `assert` statement is from the Python library and is used to verify the correctness of the code, unlike the `unittest` module which comes as a part of the Python standard library.
- The `assert` statement is used to check the condition. If the condition is `True`, the program will continue to execute. If the condition is `False`, the program will raise an `AssertionError` exception.<br/> <br/>

### Classes

- Class based test cases are used to group similar test cases together. This makes it easier to manage and run the test cases.
- Class is a blueprint for creating objects. It defines the attributes and methods that the objects will have.
- In the context of testing, a class is a blueprint for creating test cases. It defines the test methods that will be run to validate the code.
- The `unittest` module in Python provides a way to create class-based test cases.
- The `pytest` module also provides a way to create class-based test cases.
- The `pytest` module is more flexible and easier to use than the `unittest` module.

- We will start by now writing class for our test cases. We will write a simple test case to check if the given number is even or not.

    ```python
    import pytest
    testset = [(9, 5), (5, 9), (5, 4), (10, 5)]
    
    class TestCases:
    
        @pytest.mark.parametrize("a, b", testset)
        def test_greater(self,a,b):
            assert a > b, f"{a} is not greater than {b}"
    
        def test_true(self):
            assert 1
    
        def test_cmpr_string_char(self):
            assert 'ab' == "ab"
    
        @pytest.mark.parametrize("a, b", testset)
        def test_divmod(self,a,b):
            assert 1 in divmod(a,b), f"1 is not in divmod({a},{b})"
    
        def test_find_in_string(self):
            assert 'py' in 'This is pytest.'
    
        def test_is_not_in_string(self):
            assert 'put' not in 'This is pytest.'
    
        def run_tests(self):
            for a,b in testset:
                print(f"Running tests with a={a}, b={b}")
                try:
                    self.test_greater(a,b)
                    self.test_true()
                    self.test_cmpr_string_char()
                    self.test_divmod(a,b)
                    self.test_find_in_string()
                    self.test_is_not_in_string()
                    print("All tests passed")
                except AssertionError as e:
                    print(f"AssertionError: {e}")
    
    if __name__ == '__main__':
        test = TestCases()
        test.run_tests()
    ```

  Now, run the following command to run the test cases and you will obtain the output as shown below:

    ```bash
    $ pytest pytest-assertions -v
    ====================================================================== test session starts =======================================================================
    platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python
    cachedir: .pytest_cache
    rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/pytest_topics
    collected 12 items                                                                                                                                               
    
    pytest-assertions/test_module02.py::TestCases::test_greater[9-5] PASSED                                                                                    [  8%]
    pytest-assertions/test_module02.py::TestCases::test_greater[5-9] FAILED                                                                                    [ 16%]
    pytest-assertions/test_module02.py::TestCases::test_greater[5-4] PASSED                                                                                    [ 25%]
    pytest-assertions/test_module02.py::TestCases::test_greater[10-5] PASSED                                                                                   [ 33%]
    pytest-assertions/test_module02.py::TestCases::test_true PASSED                                                                                            [ 41%]
    pytest-assertions/test_module02.py::TestCases::test_cmpr_string_char PASSED                                                                                [ 50%]
    pytest-assertions/test_module02.py::TestCases::test_divmod[9-5] PASSED                                                                                     [ 58%]
    pytest-assertions/test_module02.py::TestCases::test_divmod[5-9] FAILED                                                                                     [ 66%]
    pytest-assertions/test_module02.py::TestCases::test_divmod[5-4] PASSED                                                                                     [ 75%]
    pytest-assertions/test_module02.py::TestCases::test_divmod[10-5] FAILED                                                                                    [ 83%]
    pytest-assertions/test_module02.py::TestCases::test_find_in_string PASSED                                                                                  [ 91%]
    pytest-assertions/test_module02.py::TestCases::test_is_not_in_string PASSED                                                                                [100%]
    
    ============================================================================ FAILURES ============================================================================
    __________________________________________________________________ TestCases.test_greater[5-9] ___________________________________________________________________
    
    self = <test_module02.TestCases object at 0x106abf0d0>, a = 5, b = 9
    
        @pytest.mark.parametrize("a, b", testset)
        def test_greater(self,a,b):
    >       assert a > b, f"{a} is not greater than {b}"
    E       AssertionError: 5 is not greater than 9
    E       assert 5 > 9
    
    pytest-assertions/test_module02.py:10: AssertionError
    ___________________________________________________________________ TestCases.test_divmod[5-9] ___________________________________________________________________
    
    self = <test_module02.TestCases object at 0x106abdc50>, a = 5, b = 9
    
        @pytest.mark.parametrize("a, b", testset)
        def test_divmod(self,a,b):
    >       assert 1 in divmod(a,b), f"1 is not in divmod({a},{b})"
    E       AssertionError: 1 is not in divmod(5,9)
    E       assert 1 in (0, 5)
    E        +  where (0, 5) = divmod(5, 9)
    
    pytest-assertions/test_module02.py:20: AssertionError
    __________________________________________________________________ TestCases.test_divmod[10-5] ___________________________________________________________________
    
    self = <test_module02.TestCases object at 0x106abe090>, a = 10, b = 5
    
        @pytest.mark.parametrize("a, b", testset)
        def test_divmod(self,a,b):
    >       assert 1 in divmod(a,b), f"1 is not in divmod({a},{b})"
    E       AssertionError: 1 is not in divmod(10,5)
    E       assert 1 in (2, 0)
    E        +  where (2, 0) = divmod(10, 5)
    
    pytest-assertions/test_module02.py:20: AssertionError
    ==================================================================== short test summary info =====================================================================
    FAILED pytest-assertions/test_module02.py::TestCases::test_greater[5-9] - AssertionError: 5 is not greater than 9
    FAILED pytest-assertions/test_module02.py::TestCases::test_divmod[5-9] - AssertionError: 1 is not in divmod(5,9)
    FAILED pytest-assertions/test_module02.py::TestCases::test_divmod[10-5] - AssertionError: 1 is not in divmod(10,5)
    ================================================================== 3 failed, 9 passed in 0.02s ===================================================================
    ```

## Test Discovery with Pytest

- Pytest provides a way to discover and run the test cases in a directory.
- Pytest will look for the files with the name `test_*.py` or `*_test.py`, classes with the name `Test*` and methods with the name `test_*` and `*_test`.
- Pytest will run the test cases in the order they are discovered, in parallel by default.

- Based on out folder structure, if we run the `pytest` command from `pythonProject` folder. It will execute all the test cases in all the underlying files following the conventions.

  Here's an example of that:

    <details>
    <summary>Example</summary>

    ```bash
    $  pytest -v
    ====================================================================== test session starts =======================================================================
    platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python
    cachedir: .pytest_cache
    rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
    collected 15 items                                                                                                                                               
    
    pytest_topics/pytest-assertions/test_module02.py::TestCases::test_greater[9-5] PASSED                                                                      [  6%]
    pytest_topics/pytest-assertions/test_module02.py::TestCases::test_greater[5-9] FAILED                                                                      [ 13%]
    pytest_topics/pytest-assertions/test_module02.py::TestCases::test_greater[5-4] PASSED                                                                      [ 20%]
    pytest_topics/pytest-assertions/test_module02.py::TestCases::test_greater[10-5] PASSED                                                                     [ 26%]
    pytest_topics/pytest-assertions/test_module02.py::TestCases::test_true PASSED                                                                              [ 33%]
    pytest_topics/pytest-assertions/test_module02.py::TestCases::test_cmpr_string_char PASSED                                                                  [ 40%]
    pytest_topics/pytest-assertions/test_module02.py::TestCases::test_divmod[9-5] PASSED                                                                       [ 46%]
    pytest_topics/pytest-assertions/test_module02.py::TestCases::test_divmod[5-9] FAILED                                                                       [ 53%]
    pytest_topics/pytest-assertions/test_module02.py::TestCases::test_divmod[5-4] PASSED                                                                       [ 60%]
    pytest_topics/pytest-assertions/test_module02.py::TestCases::test_divmod[10-5] FAILED                                                                      [ 66%]
    pytest_topics/pytest-assertions/test_module02.py::TestCases::test_find_in_string PASSED                                                                    [ 73%]
    pytest_topics/pytest-assertions/test_module02.py::TestCases::test_is_not_in_string PASSED                                                                  [ 80%]
    pytest_topics/test_module01.py::test_addition PASSED                                                                                                       [ 86%]
    pytest_topics/test_module01.py::test_subtraction FAILED                                                                                                    [ 93%]
    pytest_topics/test_module01.py::test_integer_division PASSED                                                                                               [100%]
    
    ============================================================================ FAILURES ============================================================================
    __________________________________________________________________ TestCases.test_greater[5-9] ___________________________________________________________________
    
    self = <test_module02.TestCases object at 0x1019b2190>, a = 5, b = 9
    
        @pytest.mark.parametrize("a, b", testset)
        def test_greater(self,a,b):
    >       assert a > b, f"{a} is not greater than {b}"
    E       AssertionError: 5 is not greater than 9
    E       assert 5 > 9
    
    pytest_topics/pytest-assertions/test_module02.py:10: AssertionError
    ___________________________________________________________________ TestCases.test_divmod[5-9] ___________________________________________________________________
    
    self = <test_module02.TestCases object at 0x1019c0810>, a = 5, b = 9
    
        @pytest.mark.parametrize("a, b", testset)
        def test_divmod(self,a,b):
    >       assert 1 in divmod(a,b), f"1 is not in divmod({a},{b})"
    E       AssertionError: 1 is not in divmod(5,9)
    E       assert 1 in (0, 5)
    E        +  where (0, 5) = divmod(5, 9)
    
    pytest_topics/pytest-assertions/test_module02.py:20: AssertionError
    __________________________________________________________________ TestCases.test_divmod[10-5] ___________________________________________________________________
    
    self = <test_module02.TestCases object at 0x1019c0d10>, a = 10, b = 5
    
        @pytest.mark.parametrize("a, b", testset)
        def test_divmod(self,a,b):
    >       assert 1 in divmod(a,b), f"1 is not in divmod({a},{b})"
    E       AssertionError: 1 is not in divmod(10,5)
    E       assert 1 in (2, 0)
    E        +  where (2, 0) = divmod(10, 5)
    
    pytest_topics/pytest-assertions/test_module02.py:20: AssertionError
    ________________________________________________________________________ test_subtraction ________________________________________________________________________
    
        def test_subtraction():
    >       assert 5 - 5 != 0, "Intentional failure 1"
    E       AssertionError: Intentional failure 1
    E       assert (5 - 5) != 0
    
    pytest_topics/test_module01.py:6: AssertionError
    ==================================================================== short test summary info =====================================================================
    FAILED pytest_topics/pytest-assertions/test_module02.py::TestCases::test_greater[5-9] - AssertionError: 5 is not greater than 9
    FAILED pytest_topics/pytest-assertions/test_module02.py::TestCases::test_divmod[5-9] - AssertionError: 1 is not in divmod(5,9)
    FAILED pytest_topics/pytest-assertions/test_module02.py::TestCases::test_divmod[10-5] - AssertionError: 1 is not in divmod(10,5)
    FAILED pytest_topics/test_module01.py::test_subtraction - AssertionError: Intentional failure 1
    ================================================================== 4 failed, 11 passed in 0.03s ==================================================================
    ```
    </details>

  Here, we can see that all the test cases in the directory are executed in the order they are discovered. The failed test cases are also shown in the output.

  For the record, we actually have a total of 15 testcases as of now. Now, you must be thinking how:
    - We have 3 testcases in `test_module01.py` file.
    - We have 12 testcases in `test_module02.py` file. Out of which:
        - 4 are constant `True` testcases.
        - 4 are `greater` testcases.
        - 4 are `divmod` testcases.

- We can also run pytests for a single file using the following command:

  ```bash
  $ pytest folder_name/sub_folder_name/.../test_something.py -v
  ```

  <details>
  <summary>Example</summary>

  ```bash
   $ pwd
   /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject

   $ pytest pytest_topics/test_module01.py -v 
   ====================================================================== test session starts =======================================================================
   platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python
   cachedir: .pytest_cache
   rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
   collected 3 items                                                                                                                                                

   pytest_topics/test_module01.py::test_addition PASSED                                                                                                       [ 33%]
   pytest_topics/test_module01.py::test_subtraction FAILED                                                                                                    [ 66%]
   pytest_topics/test_module01.py::test_integer_division PASSED                                                                                               [100%]

   ============================================================================ FAILURES ============================================================================
   ________________________________________________________________________ test_subtraction ________________________________________________________________________

   def test_subtraction():
   >       assert 5 - 5 != 0, "Intentional failure 1"
   E       AssertionError: Intentional failure 1
   E       assert (5 - 5) != 0

   pytest_topics/test_module01.py:6: AssertionError
   ==================================================================== short test summary info =====================================================================
   FAILED pytest_topics/test_module01.py::test_subtraction - AssertionError: Intentional failure 1
   ================================================================== 1 failed, 2 passed in 0.01s ===================================================================
   ```
   </details>

- Same, way we can do it for single folder as well using the command:

  ```bash
  $ pytest folder_name -v
  ```

  <details>
  <summary>Example</summary>

  ```bash
  $ pwd
  /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  $  pytest pytest_topics/pytest-assertions -v                     ✔  pythonProject   at 04:09:52  
  ====================================================================== test session starts =======================================================================
  platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python
  cachedir: .pytest_cache
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  collected 12 items                                                                                                                                               

  pytest_topics/pytest-assertions/test_module02.py::TestCases::test_greater[9-5] PASSED                                                                      [  8%]
  pytest_topics/pytest-assertions/test_module02.py::TestCases::test_greater[5-9] FAILED                                                                      [ 16%]
  pytest_topics/pytest-assertions/test_module02.py::TestCases::test_greater[5-4] PASSED                                                                      [ 25%]
  pytest_topics/pytest-assertions/test_module02.py::TestCases::test_greater[10-5] PASSED                                                                     [ 33%]
  pytest_topics/pytest-assertions/test_module02.py::TestCases::test_true PASSED                                                                              [ 41%]
  pytest_topics/pytest-assertions/test_module02.py::TestCases::test_cmpr_string_char PASSED                                                                  [ 50%]
  pytest_topics/pytest-assertions/test_module02.py::TestCases::test_divmod[9-5] PASSED                                                                       [ 58%]
  pytest_topics/pytest-assertions/test_module02.py::TestCases::test_divmod[5-9] FAILED                                                                       [ 66%]
  pytest_topics/pytest-assertions/test_module02.py::TestCases::test_divmod[5-4] PASSED                                                                       [ 75%]
  pytest_topics/pytest-assertions/test_module02.py::TestCases::test_divmod[10-5] FAILED                                                                      [ 83%]
  pytest_topics/pytest-assertions/test_module02.py::TestCases::test_find_in_string PASSED                                                                    [ 91%]
  pytest_topics/pytest-assertions/test_module02.py::TestCases::test_is_not_in_string PASSED                                                                  [100%]

  ============================================================================ FAILURES ============================================================================
  __________________________________________________________________ TestCases.test_greater[5-9] ___________________________________________________________________

  self = <test_module02.TestCases object at 0x1053f94d0>, a = 5, b = 9

  @pytest.mark.parametrize("a, b", testset) 
  def test_greater(self,a,b):
  >       assert a > b, f"{a} is not greater than {b}"
  E       AssertionError: 5 is not greater than 9
  E       assert 5 > 9

  pytest_topics/pytest-assertions/test_module02.py:10: AssertionError
  ___________________________________________________________________ TestCases.test_divmod[5-9] ___________________________________________________________________

  self = <test_module02.TestCases object at 0x105408650>, a = 5, b = 9

  @pytest.mark.parametrize("a, b", testset)
  def test_divmod(self,a,b):
  >       assert 1 in divmod(a,b), f"1 is not in divmod({a},{b})"
  E       AssertionError: 1 is not in divmod(5,9)
  E       assert 1 in (0, 5)
  E        +  where (0, 5) = divmod(5, 9)

  pytest_topics/pytest-assertions/test_module02.py:20: AssertionError
  __________________________________________________________________ TestCases.test_divmod[10-5] ___________________________________________________________________

  self = <test_module02.TestCases object at 0x105408b50>, a = 10, b = 5

  @pytest.mark.parametrize("a, b", testset) 
  def test_divmod(self,a,b):
  >       assert 1 in divmod(a,b), f"1 is not in divmod({a},{b})"
  E       AssertionError: 1 is not in divmod(10,5)
  E       assert 1 in (2, 0)
  E        +  where (2, 0) = divmod(10, 5)

  pytest_topics/pytest-assertions/test_module02.py:20: AssertionError
  ==================================================================== short test summary info =====================================================================
  FAILED pytest_topics/pytest-assertions/test_module02.py::TestCases::test_greater[5-9] - AssertionError: 5 is not greater than 9
  FAILED pytest_topics/pytest-assertions/test_module02.py::TestCases::test_divmod[5-9] - AssertionError: 1 is not in divmod(5,9)
  FAILED pytest_topics/pytest-assertions/test_module02.py::TestCases::test_divmod[10-5] - AssertionError: 1 is not in divmod(10,5)
  ================================================================== 3 failed, 9 passed in 0.02s ===================================================================
  ```
  </details>

- The surprising part is we can run pytest using class name as well. Here's how you can do it:

  ```bash
  $ pytest folder_name/sub_folder_name/.../test_something.py::ClassName -v
  ```

    <details>
    <summary>Example</summary>

    ```bash
    $ pwd
    /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
    $ pytest pytest_topics/pytest-assertions/test_module02.py::TestCases -v
    ====================================================================== test session starts =======================================================================
    platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python
    cachedir: .pytest_cache
    rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
    collected 12 items                                                                                                                                               
    
    pytest_topics/pytest-assertions/test_module02.py::TestCases::test_greater[9-5] PASSED                                                                      [  8%]
    pytest_topics/pytest-assertions/test_module02.py::TestCases::test_greater[5-9] FAILED                                                                      [ 16%]
    pytest_topics/pytest-assertions/test_module02.py::TestCases::test_greater[5-4] PASSED                                                                      [ 25%]
    pytest_topics/pytest-assertions/test_module02.py::TestCases::test_greater[10-5] PASSED                                                                     [ 33%]
    pytest_topics/pytest-assertions/test_module02.py::TestCases::test_true PASSED                                                                              [ 41%]
    pytest_topics/pytest-assertions/test_module02.py::TestCases::test_cmpr_string_char PASSED                                                                  [ 50%]
    pytest_topics/pytest-assertions/test_module02.py::TestCases::test_divmod[9-5] PASSED                                                                       [ 58%]
    pytest_topics/pytest-assertions/test_module02.py::TestCases::test_divmod[5-9] FAILED                                                                       [ 66%]
    pytest_topics/pytest-assertions/test_module02.py::TestCases::test_divmod[5-4] PASSED                                                                       [ 75%]
    pytest_topics/pytest-assertions/test_module02.py::TestCases::test_divmod[10-5] FAILED                                                                      [ 83%]
    pytest_topics/pytest-assertions/test_module02.py::TestCases::test_find_in_string PASSED                                                                    [ 91%]
    pytest_topics/pytest-assertions/test_module02.py::TestCases::test_is_not_in_string PASSED                                                                  [100%]
    
    ============================================================================ FAILURES ============================================================================
    __________________________________________________________________ TestCases.test_greater[5-9] ___________________________________________________________________
    
    self = <test_module02.TestCases object at 0x105d4d990>, a = 5, b = 9
    
        @pytest.mark.parametrize("a, b", testset)
        def test_greater(self,a,b):
    >       assert a > b, f"{a} is not greater than {b}"
    E       AssertionError: 5 is not greater than 9
    E       assert 5 > 9
    
    pytest_topics/pytest-assertions/test_module02.py:10: AssertionError
    ___________________________________________________________________ TestCases.test_divmod[5-9] ___________________________________________________________________
    
    self = <test_module02.TestCases object at 0x105d4ff50>, a = 5, b = 9
    
        @pytest.mark.parametrize("a, b", testset)
        def test_divmod(self,a,b):
    >       assert 1 in divmod(a,b), f"1 is not in divmod({a},{b})"
    E       AssertionError: 1 is not in divmod(5,9)
    E       assert 1 in (0, 5)
    E        +  where (0, 5) = divmod(5, 9)
    
    pytest_topics/pytest-assertions/test_module02.py:20: AssertionError
    __________________________________________________________________ TestCases.test_divmod[10-5] ___________________________________________________________________
    
    self = <test_module02.TestCases object at 0x105d58490>, a = 10, b = 5
    
        @pytest.mark.parametrize("a, b", testset)
        def test_divmod(self,a,b):
    >       assert 1 in divmod(a,b), f"1 is not in divmod({a},{b})"
    E       AssertionError: 1 is not in divmod(10,5)
    E       assert 1 in (2, 0)
    E        +  where (2, 0) = divmod(10, 5)
    
    pytest_topics/pytest-assertions/test_module02.py:20: AssertionError
    ==================================================================== short test summary info =====================================================================
    FAILED pytest_topics/pytest-assertions/test_module02.py::TestCases::test_greater[5-9] - AssertionError: 5 is not greater than 9
    FAILED pytest_topics/pytest-assertions/test_module02.py::TestCases::test_divmod[5-9] - AssertionError: 1 is not in divmod(5,9)
    FAILED pytest_topics/pytest-assertions/test_module02.py::TestCases::test_divmod[10-5] - AssertionError: 1 is not in divmod(10,5)
    ================================================================== 3 failed, 9 passed in 0.02s ===================================================================
    ```
    </details>

- We can also do the same using the method name as well. Here's how you can do it:

  ```bash
  $ pytest folder_name/sub_folder_name/.../test_something.py::ClassName::method_name -v
  ```

  <details>
  <summary>Example</summary>

  ```bash
  $ pwd
  /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  $  pytest pytest_topics/test_module01.py::test_addition -v
  ====================================================================== test session starts =======================================================================
  platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python
  cachedir: .pytest_cache
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  collected 1 item                                                                                                                                                 

  pytest_topics/test_module01.py::test_addition PASSED                                                                                                       [100%]

  ======================================================================= 1 passed in 0.00s ========================================================================
  ```

  </details>

  This is really helpful when you want to run a single test case from a file containing multiple test cases.

<hr/>

### About `__init__.py`

- When we created the Python Package not a normal folder because we wanted `__init__.py` file to be created in the folder.
- The `__init__.py` file is used to mark the directory as a Python package directory. And it let's us create same file name in multiple subdirectories.

<hr/>

## pytest.raises Assertion

- So, basically let's say we are aware that we have a test where we know we are going to get an exception from one of our tests, and we want to test that scenario. Let's say we have a scenario where it throws an exception error like 500 internal error or something like a 400 error, and we want to test that scenario, and we know that is the correct behavior.

- If we write it down like a normal test case the resultant will show it as a `Failure` Test Case. But, we don't want the test to fail, and want to check that API Call actually throws an exception and, we are sure that our function is working properly in that scenario as well. These kinds of exercises are highly used in Unit or Integration test scenarios where we are actually expecting
  an exception or an anomaly from our application under test.

- And, if we don't get the exception than in that scenario it's not correct, basically a negative true scenario. So, in that scenario if there's an Assertion error we want the test to be passed, and move ahead with the next test. If it doesnot throw any error this should fail the test.

- Let's understand this through an example: 
  
  ```python
  import pytest
  
  def test_testing():
      with pytest.raises(Exception):
          assert (1/0), f"ZeroDivisionError"
  ```

  Now, run the `pytest` command and inspect the output:

  ```bash
  pytest -v pytest_topics/pytest-assertions/test_module03.py 
  =================================================================== test session starts ====================================================================
  platform darwin -- Python 3.11.3, pytest-7.4.2, pluggy-1.3.0 -- /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
  cachedir: .pytest_cache
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  plugins: django-4.5.2
  collected 1 item                                                                                                                                           
  
  pytest_topics/pytest-assertions/test_module03.py::test_testing PASSED                                                                                [100%]
  
  ==================================================================== 1 passed in 0.01s =====================================================================
  ```

  We can clearly see that the test case is passed even though this is an exceptional case.

- Let's take another great example:

  `test_module03.py`

  ```python
  import pytest
  import re
  import requests
  
  testset = [(1,2),(2,1)]
  
  class TestCases:
      def test_zero_divisibility(self):
          with pytest.raises(Exception):
              assert (1/0)
  
      @pytest.mark.parametrize("a, b", testset)
      def test_equation(self,a,b):
          summ = a+b
          diff = a-b
          asq = a*a
          bsq = b*b
          lhs = summ * diff
          rhs = asq - bsq
          assert lhs == rhs
  
      def test_404(self):
          with pytest.raises(Exception):
              assert requests.get("https://httpbin.org/status/404"), f"404 Response Code"
  
      def run_tests(self):
          self.test_zero_divisibility()
          self.test_404()
  
          for a,b in testset:
              try:
                  self.test_equation(a,b)
              except AssertionError as e:
                  print(f"AssertionError: {e}")
  
  if __name__ == '__main__':
      test = TestCases()
      test.run_tests()
  ```
  
  Now, run the command `pytest`, and inspect the output:

  ```bash
  $  pytest -v pytest_topics/pytest-assertions/test_module03.py
  =================================================================== test session starts ====================================================================
  platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python
  cachedir: .pytest_cache
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  collected 4 items                                                                                                                                          

  pytest_topics/pytest-assertions/test_module03.py::TestCases::test_zero_divisibility PASSED                                                           [ 25%]
  pytest_topics/pytest-assertions/test_module03.py::TestCases::test_equation[1-2] PASSED                                                               [ 50%]
  pytest_topics/pytest-assertions/test_module03.py::TestCases::test_equation[2-1] PASSED                                                               [ 75%]
  pytest_topics/pytest-assertions/test_module03.py::TestCases::test_404 PASSED                                                                         [100%]

  ==================================================================== 4 passed in 1.35s =====================================================================
  ```
  
- We can also inspect the exception that came out of our test, and we want to assert on that exception, for that let's write another test case.

  ```python
  def test_tuple_cmpr(self):
    with pytest.raises(Exception) as e:
        assert (1,2,3) == (1,2,4)
    print(e)
  ```
  
  If you execute pytest command and specifically run this test, you will get the following output:

  ```bash
  $ pytest
  /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python /Users/akd/Applications/PyCharm Community Edition.app/Contents/plugins/python-ce/helpers/pycharm/_jb_pytest_runner.py --target test_module03.py::TestCases.test_tuple_cmpr 
  Testing started at 7:51 am ...
  Launching pytest with arguments test_module03.py::TestCases::test_tuple_cmpr --no-header --no-summary -q in /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/pytest_topics/pytest-assertions
  
  ============================= test session starts ==============================
  collecting ... collected 1 item
  
  test_module03.py::TestCases::test_tuple_cmpr PASSED                      [100%]<ExceptionInfo AssertionError('assert (1, 2, 3) == (1, 2, 4)\n  \n  At index 2 diff: 3 != 4\n  \n  Full diff:\n    (\n        1,\n        2,\n  -     4,\n  ?     ^\n  +     3,\n  ?     ^\n    )') tblen=1>
  
  
  ============================== 1 passed in 0.07s ===============================
  
  Process finished with exit code 0
  ```

  And, here we get the line `<ExceptionInfo AssertionError('assert (1, 2, 3) == (1, 2, 4)\n  \n  At index 2 diff: 3 != 4\n  \n  Full diff:\n    (\n        1,\n        2,\n  -     4,\n  ?     ^\n  +     3,\n  ?     ^\n    )') tblen=1>` clearly specifying the error.

- Let's say we have another exception being raised by a different function, we can also assert that as well, and assert that, we can do it as follows:

  ```python
  import pytest
  import re
  import requests
  
  testset = [(1,2),(2,1)]
  
  def func1():
      raise ValueError("Exception func1")
  
  class TestCases:
      def test_zero_divisibility(self):
          with pytest.raises(Exception):
              assert (1/0)
  
      @pytest.mark.parametrize("a, b", testset)
      def test_equation(self,a,b):
          summ = a+b
          diff = a-b
          asq = a*a
          bsq = b*b
          lhs = summ * diff
          rhs = asq - bsq
          assert lhs == rhs
  
      def test_404(self):
          with pytest.raises(Exception):
              assert requests.get("https://httpbin.org/status/404"), f"404 Response Code"
  
      def test_error_assert(self):
          with pytest.raises(Exception) as e:
              func1()
          print(str(e))
          assert (str(e.value)) == "Exception func1"
  
      def test_tuple_cmpr(self):
          with pytest.raises(Exception) as e:
              assert (1,2,3) == (1,2,4)
  
      def run_tests(self):
          self.test_zero_divisibility()
          self.test_404()
  
          for a,b in testset:
              try:
                  self.test_equation(a,b)
              except AssertionError as e:
                  print(f"AssertionError: {e}")
  
  if __name__ == '__main__':
      test = TestCases()
      test.run_tests()  
  ```
  
  Run the command `pytest` and inspect the output:

  ```bash
  $ pytest -v ./pytest_topics/pytest-assertions/test_module03.py
  =================================================================== test session starts ====================================================================
  platform darwin -- Python 3.11.3, pytest-7.4.2, pluggy-1.3.0 -- /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
  cachedir: .pytest_cache
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  plugins: django-4.5.2
  collected 6 items                                                                                                                                          
  
  pytest_topics/pytest-assertions/test_module03.py::TestCases::test_zero_divisibility PASSED                                                           [ 16%]
  pytest_topics/pytest-assertions/test_module03.py::TestCases::test_equation[1-2] PASSED                                                               [ 33%]
  pytest_topics/pytest-assertions/test_module03.py::TestCases::test_equation[2-1] PASSED                                                               [ 50%]
  pytest_topics/pytest-assertions/test_module03.py::TestCases::test_404 PASSED                                                                         [ 66%]
  pytest_topics/pytest-assertions/test_module03.py::TestCases::test_error_assert PASSED                                                                [ 83%]
  pytest_topics/pytest-assertions/test_module03.py::TestCases::test_tuple_cmpr PASSED                                                                  [100%]
  
  ==================================================================== 6 passed in 1.34s =====================================================================
  ```
  
  Hence, we can also raise our own ValueError and assert it, and pass the test case.