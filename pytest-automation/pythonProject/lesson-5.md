# Pytest: Customizations

- When we want to test with multiple environments, we can just toss in some arguments in our commandline and, we can actually design our test in such a way that based on the command line arguments, we can execute our test in production or development if we want to.
- In this chapter, we will be looking into how we can pass in command line arguments to our pytest test functions.
- For this we will be using something called `hooks`, Initialization hooks in pytest.
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

- This way we can use the command line to pass arguments or inputs to the tests.

## Configuring Pytest

- Many pytest settings can be set in a configuration file, which by convention resides in the root directory of your repository.

### `pytest.ini`

- `pytest.ini` files take precedence over other files, even when empty.
- Must be placed in the root folder of the project.
- This is the most common way of configuring the pytests.
- Example:

	```ini
	[pytest]
	addopts = -v --color=yes
	testpaths = tests integration_tests
	norecursedirs = .venv node_modules
	markers =
	    slow: marks tests as slow
	    integration: integration tests
	python_files = test_*.py *_test.py
	python_classes = Test* *Suite
	python_functions = test_* check_*
	xfail_strict = true
	```
 
### `pyproject.toml`

- pyproject.toml are considered for configuration when they contain a tool.pytest.ini_options table.
- Example:

	```toml
	[tool.pytest.ini_options]
	addopts = ["-v", "--tb=short"]
	testpaths = ["tests"]
	markers = [
	    "smoke: quick validation tests",
	    "performance: benchmark tests"
	]
	filterwarnings = [
	    "error::UserWarning"
	]
	
	[tool.coverage.run]
	source = ["src"]
	```
 
### `tox.ini`

- `tox.ini` files are the configuration files of the tox project, and can also be used to hold pytest configuration if 
  they have a [pytest] section.
- Example:

	```ini
	[tox]
	envlist = py38, py39
	
	[pytest]
	addopts = --junitxml=reports/junit.xml
	python_files = test_*.py
	minversion = 6.0
	
	[testenv]
	deps = pytest
	commands = pytest tests/
	```

### `setup.cfg`

- `setup.cfg` files are general purpose configuration files, used originally by distutils (now deprecated) and 
  setuptools, and can also be used to hold pytest configuration if they have a [tool:pytest] section.
- Examples:

	```ini
	[metadata]
	name = myproject
	
	[tool:pytest]
	addopts = --durations=10
	norecursedirs = .* venv
	```
 
<center>
<table>
	<tr>
		<th>Format</th>
		<th>File Extension</th>
		<th>Syntax</th>
		<th>Pros</th>
		<th>cons</th>
	</tr>
	<tr>
		<td><code>INI</code></td>
		<td> <code>.ini</code></td>
		<td>Simple</td>
		<td>Wide Support, Human Readable</td>
		<td>Limited Datatypes</td>
	</tr>
	<tr>
		<td><code>TOML</code></td>
		<td> <code>.toml</code></td>
		<td>Modern</td>
		<td>PEP 621 Standard, Rich types</td>
		<td>Newer Format</td>
	</tr>
	<tr>
		<td><code>setup.cfg</code></td>
		<td> <code>.cfg</code></td>
		<td>Legacy</td>
		<td>Shared with setuptools</td>
		<td>Depreceated for Pytest</td>
	</tr>
	<tr>
		<td><code>tox.ini</code></td>
		<td> <code>.ini</code></td>
		<td>Shared</td>
		<td>Good for tox integration</td>
		<td>Not pytest specific</td>
	</tr>
</table>
</center>

- It is mostly recommended to use `pytest.ini` file, for configuring the pytests. If you want to go through the 
  details of some of the options available for `pytest.ini`, we recommend you to go to the documentation page to 
  explore more on that.

## Dataprovider (Data Driven Tests)

- In this section, we will see how we can pass in data from our file, and use the data to run our test.
- In a real environment, in an actual automation framework, we need to read data  or input values from file and 
  actually work on top of that.
- We can do the same in `pytest` using `@pytest.mark.paramaterize()` to pass data after reading from the file.
- Let's start by creating a python package named `utils`.

  ![](./imgs/Screenshot%202025-04-15%20at%209.20.50%E2%80%AFPM.png)
  <br/>
  ![](./imgs/Screenshot%202025-04-15%20at%209.23.48%E2%80%AFPM.png)

- And, we will have a csv file inside the `config` folder, you will find it in our doler structure if you look 
  carefully. You can place it another place also, we are just doing it for our own convinence and organizing purpose.

- Here's our csv file for you:

	```csv
	age,name,salary(lpa),city
	24,aman,21,banaglore
	25,aziz,25,Gurgaon
	26,Harikesh,26,Bangalore
	25,Ayush,4.2,Raipur
	```
 
- Now, in `utils` folder create a `utils.py` file where we will read this csv file.

	`utils.py`
	
	```python
	import csv
	from pathlib import Path
	
	dataFile = "data.csv"
	cfgFileDir = 'config'
	
	BASE_DIR = Path(__file__).resolve().parent.parent
	DATA_FILE = BASE_DIR.joinpath(cfgFileDir).joinpath(dataFile)
	
	def get_data():
	    with open(DATA_FILE,'r+') as f:
	        reader = csv.reader(f)
	        next(reader) # Skips the first row, as it has the header
	        data = [tuple(row) for row in reader]
	
	    return data
	
	print(get_data())
	```

- When this program `utils.py` is executed, you see it return a list of tuples.

  ![](./imgs/Screenshot%202025-04-15%20at%209.41.31%E2%80%AFPM.png)

- So, now we know our function is working properly. Now, next thing we need to do is write our test here.

	`test_dataProvider.py`
	
	```python
	import pytest
	from pytest_topics.utils.utils import get_data
	
	class TestCases:
	
	    @pytest.mark.parametrize("a,b,c,d",get_data())
	    def test_checkFileData(self,a,b,c,d):
	        print(f"{b}'s  age is {a}.")
	```
 
- Once you execute, you get the following output:

	```bash
	$ pytest -v -s test_dataProvider.py                                                 ✔  at 21:52:00  
	============================================================================ test session starts =============================================================================
	platform darwin -- Python 3.11.3, pytest-7.4.2, pluggy-1.3.0 -- /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
	cachedir: .pytest_cache
	rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
	configfile: pytest.ini
	plugins: django-4.5.2
	collecting ... [('24', 'aman', '21', 'banaglore'), ('25', 'aziz', '25', 'Gurgaon'), ('26', 'Harikesh', '26', 'Bangalore'), ('25', 'Ayush', '4.2', 'Raipur')]
	collected 4 items                                                                                                                                                            
	
	test_dataProvider.py::TestCases::test_checkFileData[24-aman-21-banaglore] aman's  age is 24.
	PASSED
	test_dataProvider.py::TestCases::test_checkFileData[25-aziz-25-Gurgaon] aziz's  age is 25.
	PASSED
	test_dataProvider.py::TestCases::test_checkFileData[26-Harikesh-26-Bangalore] Harikesh's  age is 26.
	PASSED
	test_dataProvider.py::TestCases::test_checkFileData[25-Ayush-4.2-Raipur] Ayush's  age is 25.
	PASSED
	
	============================================================================= 4 passed in 0.01s ==============================================================================
	```

- Using this way you can do a real world Data Driven Testing.

## Using Configuration Files

- So, far we have used fixtures for data driven tests. Now, we will use what we have learnt to start utilising the 
  config file for the same purpose.
- This will be really helpful as all type of projects need some type of configuration.
- It it's a test automation project, we need to test against different environments, to say the least each 
  environment can have different url, login, passwords and, things like that.
- Config files are important for test automation project as we cannot hardcode the values like login IDs, username 
  or password. Also, there can be too many configurations in some of these cases which we wdon't want to include in 
  the code, which become cumbersome to edit it later in multiple places.
- If it's within the code, we don't want to edit the code for editing the configurations.
- As, we have discussed in python we can have config files in different formats like `JSON`, `HTML`, `YAML` or `ini` 
  format.
- In this particular section, we will see how we can readan `*.ini` format file in our test automation.

- Let's start by first creating our config file `qa.ini`

	`qa.ini`
	
	```ini
	[gmail]
	url = qa.gmail.com
	user = gamil_user1
	pass = gamil_pass1
	
	[outlook]
	url = qa.outlook.com
	user = outlook_user1
	pass = outlook_pass1
	```
 
- In the `utils` folder create  we wil put our config parser. Let's name it as `myconfigparser.py`.
- Here, we could have written this program following OOPs, like for example creating a class, and all those things, 
  but for learning purpose we are simplifying it here.

	`myconfigparser.py`
	
	```python
	import configparser
	from pathlib import Path
	
	cfgFile = 'qa.ini'
	cfgFileDirectory = 'config'
	
	# Here, we initialise the configparser module, and will use the config variable to read the config file.
	config = configparser.ConfigParser()
	
	
	BASE_DIR = Path(__file__).resolve().parent.parent
	CONFIG_FILE = BASE_DIR.joinpath(cfgFileDirectory).joinpath(cfgFile)
	
	config.read(CONFIG_FILE)
	
	def getGmailUrl():
	    return config['gmail']['url']
	
	def getGmailUsr():
	    return config['gmail']['user']
	
	def getGmailPass():
	    return config['gmail']['pass']
	
	def getOutlookUrl():
	    return config['outlook']['url']
	
	def getOutlookUsr():
	    return config['outlook']['user']
	
	def getOutlookPass():
	    return config['outlook']['pass']
	```
 
- Once, this is done we can writting our testcases. Create a test file named `test_getConfigData.py`, and write down 
  a simple test.

	`test_getConfigData.py`

	```python
	import pytest
	from pytest_topics.utils.myconfigparser import *
	
	class TestCases:
	
	    def test_getGmailUrl(self):
	        try:
	            print(f"Gmail URL: {getGmailUrl()}")
	            assert getGmailUrl() == 'qa.gmail.com'
	        except Exception as e:
	            print(f"Unknown Error Occured: {e}.")
	
	
	
	if __name__ == '__main__':
	    test = TestCases()
	```
 
- Now, execute the test, and see if we can access the config data or not.

	```bash
	$ pytest -v -s test_getConfigData.py                                                  ✔  at 00:39:27  
	============================================================================ test session starts =============================================================================
	platform darwin -- Python 3.11.3, pytest-7.4.2, pluggy-1.3.0 -- /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
	cachedir: .pytest_cache
	rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
	configfile: pytest.ini
	plugins: django-4.5.2
	collected 1 item                                                                                                                                                             
	
	test_getConfigData.py::TestCases::test_getGmailUrl Gmail URL: qa.gmail.com
	PASSED
	============================================================================= 1 passed in 0.01s ==============================================================================
	```

- Now, we know how to write a `configparser` and read a config file using it, and use it properly in the test.
- In the current way of writing the `configparser`, we cannot control which config file to read. We want to be more 
  dynamic, and read config files based on the environment we are testing, but we don't want to hardcode the config 
  file name in our `configparser`. We don't want to hardcode the config file path here, but we want to be able to 
  pass in the config file name from where we are calling our test.
- For example, let's say we want to test in production, and now we would need to go into the code and change it 
  which is really a very tedious task to do again and again.
- So, we will need to use the Object Oriented way of writing the `ocnfigparser` in classes and object, which will 
  really help in controlling what we pass into the `configparser`, based on which we can control our testing 
  environment.
- Let's write another `configparser`:

	`configParserOOP.py`

	```python
	import configparser
	from pathlib import Path
	
	from setuptools.command.setopt import config_file
	
	
	class ConfigParser():
	
	    cfgFile = 'qa.ini' # default config file
	    cfgFileDirectory = 'config' # config directory
	
	    config = configparser.ConfigParser()
	
	    # Next, we will start by creating a constructor for the clas
	    def __init__(self, cfg=cfgFile):
	        self.cfgFile = cfg
	        self.BASE_DIR = Path(__file__).resolve().parent.parent
	        self.CONFIG_FILE = self.BASE_DIR.joinpath(self.cfgFileDirectory).joinpath(self.cfgFile)
	        self.config.read(self.CONFIG_FILE)
	
	    def getGmailUrl(self):
	        return self.config['gmail']['url']
	
	
	    def getGmailUsr(self):
	        return self.config['gmail']['user']
	
	
	    def getGmailPass(self):
	        return self.config['gmail']['pass']
	
	
	    def getOutlookUrl(self):
	        return self.config['outlook']['url']
	
	
	    def getOutlookUsr(self):
	        return self.config['outlook']['user']
	
	
	    def getOutlookPass():
	        return config['outlook']['pass']
	```
 
- Created another `ini` file for prod configurations.

	`prod.ini`
	
	```ini
	[gmail]
	url = qa_prod.gmail.com
	user = gamil_prod_user1
	pass = gamil_prod_pass1
	
	[outlook]
	url = qa_prod.outlook.com
	user = outlook_prod_user1
	pass = outlook_prod_pass1
	```

- Create the test file for testing the access to the config file as per the arguments passed to the `configparser`.

	`test_getConfigData.py`
	
	```python
	import pytest
	from pytest_topics.utils.configParserOOP import ConfigParser
	
	config  = ConfigParser('prod.ini')
	class TestCases():
	
	    def test_getGmailUrl_qa(self):
	        assert config.getGmailUrl() == 'qa.gmail.com'
	
	    def test_getGmailUrl_prod(self):
	        assert config.getGmailUrl() == 'qa_prod.gmail.com'
	
	
	
	
	if __name__ == '__main__':
	    test = TestCases()
	```
  
- Now, execute this and you will see the following output:

	```bash
	$ pytest -v -s test_getConfigData.py                                                1 ✘  at 01:20:40  
	============================================================================ test session starts =============================================================================
	platform darwin -- Python 3.11.3, pytest-7.4.2, pluggy-1.3.0 -- /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
	cachedir: .pytest_cache
	rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
	configfile: pytest.ini
	plugins: django-4.5.2
	collected 2 items                                                                                                                                                            
	
	test_getConfigData.py::TestCases::test_getGmailUrl_qa FAILED
	test_getConfigData.py::TestCases::test_getGmailUrl_prod PASSED
	
	================================================================================== FAILURES ==================================================================================
	_______________________________________________________________________ TestCases.test_getGmailUrl_qa ________________________________________________________________________
	
	self = <pytest_topics.test_getConfigData.TestCases object at 0x104973b10>
	
	    def test_getGmailUrl_qa(self):
	>       assert config.getGmailUrl() == 'qa.gmail.com'
	E       AssertionError: assert 'qa_prod.gmail.com' == 'qa.gmail.com'
	E         - qa.gmail.com
	E         + qa_prod.gmail.com
	E         ?   +++++
	
	test_getConfigData.py:8: AssertionError
	========================================================================== short test summary info ===========================================================================
	FAILED test_getConfigData.py::TestCases::test_getGmailUrl_qa - AssertionError: assert 'qa_prod.gmail.com' == 'qa.gmail.com'
	======================================================================== 1 failed, 1 passed in 0.14s =========================================================================
	```
 
- Cause in the testcase we have clearly mentioned, that the testing should cove the `prod.ini` configurations, which 
  overwrites the default reading of `qa.ini` file.