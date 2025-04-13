# Pytest: Paramaterized Tests

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