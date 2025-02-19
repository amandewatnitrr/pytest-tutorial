# Pytest Assertions and Test Discovery

![](./imgs/Getting-Started-with-Testing-in-Python_Watermarked.webp)

## Assertions & Class Based Test Cases

- Assertions are way of validating our tests. They are the main component of the test.
- Unless you validate what you are exepcting, you can't be sure if your test is passing or failing.
- The `assert` statement is from the Python library and is used to verify the correctness of the code, unlike the `unittest` module which comes as a part of the Python standard library.
- The `assert` statement is used to check the condition. If the condition is `True`, the program will continue to execute. If the condition is `False`, the program will raise an `AssertionError` exception.<br/> <br/>

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
    rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/pytest-topics
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
