# Pytest: Customizations

- When we want to test with multiple environments, we can just toss in some arguments in our commandline and, we can actually design our test in such a way that based on the command line arguments, we can execute our test in production or development if we want to.
- In this chapter, we will be looking into how we can pass in command line arguments to our pytest test functions.
- For this we will be using something called `hooks`, Initializtion hooks in pytest.
- And, we need to use a special function `pytest_addoption` function and, that works in conjunction with the fixture. `conftest.py` file which we have seen earlier in the fixture topic in that file, we need to define a function.
- And, the other thing which we need to take note of is that the `conftest.py` file we define should be in the root folder of our project.
- We will need to pass the `parser` parameter to the `pytest_addoption(parser)` function which will actually pass the command line arguments, and give us the options that we want.
- Let's try to understand this through an example:

	`conftest.py`
	
	```python
	import pytest
	
	def pytest_addoption(parser):
	    parser.addoption("--cmdopt",default='QA')
	```

- In this case what we are trying to do here is, we will provide some command line option, and based on the input it will read some file from the folder, and it will bring something out of that file.
- What we wrote above so far is our hook function. And, what we need to do is, we are getting the parser argument passed and, we get the parameter `--cmdopt`. Now, we need to define a fixture reading this command line option.
- Let's update our `conftest.py` file to update this:

	`conftest.py`
	
	```python
	qa_prop = 'qa.prop'
	prod_prop = 'prod.prop'
	
	# This is the hook, that asks the parser attribute to look for similar option when executing the test from the command line.
	def pytest_addoption(parser):
	    parser.addoption("--cmdopt",default='qa')
	
 	# This is the defined fixture, which takes value from the given option defined by the hook, and than accepts the value.
	@pytest.fixture()
	def cmdOpt(pytestconfig):
	    opt = pytestconfig.getoption("cmdopt")
	    if opt == 'qa':
	        f = open("qa.prop",'r+')
	    elif opt == 'prod':
	        f = open("prod.prop",'r+')
	    else:
	        f = open("unknown.prop",'r+')
	    yield f
	```
 
	`test_customization.py`
	
	```python
	import pytest
	
	class TestCases:
	
	    def test_readCmdOpt(self,cmdOpt):
	        print(f"Reading the config file: {cmdOpt.readline()}")
	```
 
- `pytestconfig` is again special fixture in pytest using this we can read the command line option that we mention to be read from the command line using the `parser` attribute.
- Once we execute this, we will get the following output for the given options:

	```bash
	 $  pytest -v -s test_customization.py                                             ✔  at 18:06:05  
	 ========================================================================== test session starts ==========================================================================
	 platform darwin -- Python 3.11.3, pytest-7.4.2, pluggy-1.3.0 -- /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
	 cachedir: .pytest_cache
	 rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
	 configfile: pytest.ini
	 plugins: django-4.5.2
	 collected 1 item                                                                                                                                                        
	 
	 test_customization.py::TestCases::test_readCmdOpt Reading the config file: QA Lab Details
	 PASSED
	 =========================================================================== 1 passed in 0.00s ===========================================================================
	```
 
	```bash
	 pytest -v -s test_customization.py --cmdopt=prod            
	 ========================================================================== test session starts ==========================================================================
	 platform darwin -- Python 3.11.3, pytest-7.4.2, pluggy-1.3.0 -- /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
	 cachedir: .pytest_cache
	 rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
	 configfile: pytest.ini
	 plugins: django-4.5.2
	 collected 1 item                                                                                                                                                        
	 
	 test_customization.py::TestCases::test_readCmdOpt Reading the config file: Prod Lab Details
	 PASSED
	 =========================================================================== 1 passed in 0.00s ===========================================================================
	```
 
- One example, where we have mentioned no option, it took `qa` as a default option. It reads the `qa.prop` file.
- While, in the other where we have given them command line argument `--cmdopt=prod`, it has specifically read the 
  `prod.prop` file.