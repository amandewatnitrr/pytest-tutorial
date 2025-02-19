# Pytest Automation

![](./imgs/BLOG_PyTest-–-A-Python-Solution-For-Test-Automation-1024x535%201.png)

## Instructions

- The project is created using Pycharm Community Edition, so we directly specified  the need for a `venv`.
- You can activate the virtual environment by running the command:
  
  ```bash
  $ source .venv/bin/activate
  ```

- If you want to deactivate the virtual environment, you can run the command:
  
  ```bash
  $ deactivate
  ```

> [!WARNING]
> For this tutorial, we won't cover any other basics of python, so you should have a basic understanding of python.

- So, create a python directory, in our case `pytest-topics`, and inside it you will have a `__init__.py` file.
- There create a file following the name convention `test_something.py`.
- `pytest` will automatically detect the file and run the tests.

- Our file structure would look something like this:
  
  ```bash
  $ tree                                                                                             ✔  pythonProject   at 18:40:19  
  .
  ├── README.md
  └── pytest-automation
      └── pythonProject
          ├── imgs
          │   └── BLOG_PyTest-–-A-Python-Solution-For-Test-Automation-1024x535 1.png
          ├── lesson-1.md
          └── pytest-topics
              ├── __init__.py
              ├── __pycache__
              │   ├── __init__.cpython-311.pyc
              │   └── test_module01.cpython-311-pytest-8.3.4.pyc
              └── test_module01.py
  
  6 directories, 7 files
  ```

- In a similar fashion, our `pytest` functions should also follow the naming convention as shown below:

  ```python
  def test_function_name():
      pass
  ```
  
- The `test` keyword is mandatory for `pytest` to detect the function as a test function.
- Now, let's start by writing a simple test function: <br/><br/>

  `test_module01.py`

  ```python
  def test_addition():
      assert 5 + 5 == 10
  ```
  
- Now, to run the test, you can run the command, from `pythonProject` directory:
  
  ```bash
  $ pytest pytest-topics
  ```
  
- You will see output something like this:

  ```bash
  $ pytest pytest-topics
  =================================================================== test session starts ===================================================================
  platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  collected 1 item                                                                                                                                          

  pytest-topics/test_module01.py .                                                                                                                    [100%]
  ==================================================================== 1 passed in 0.00s ====================================================================
  ```
  
- You can see that the test passed successfully.

- Let's tweak around the test a bit and see what happens when the test fails:<br/><br/>

  `test_module01.py`

  ```python
  def test_true():
    assert 5 + 5 == 11

  def test_false():
      assert 5 + 5 != 10
  ```
  
  The output looks something like this:

  ```bash
  $ pytest pytest-topics
  ==================================================================== test session starts ====================================================================
  platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  collected 2 items                                                                                                                                           

  pytest-topics/test_module01.py .F                                                                                                                     [100%]

  ========================================================================= FAILURES ==========================================================================
  ________________________________________________________________________ test_false _________________________________________________________________________

      def test_false():
  >       assert 5 + 5 != 10
  E       assert (5 + 5) != 10

  pytest-topics/test_module01.py:5: AssertionError
  ================================================================== short test summary info ==================================================================
  FAILED pytest-topics/test_module01.py::test_false - assert (5 + 5) != 10
  ================================================================ 1 failed, 1 passed in 0.01s ================================================================
  ```
  
- We can see that the test failed, and the output shows the failed test. It also shows that 1 test passed and 1 failed.
- It clearly shows the assertion error and the line where the error occurred.

- Let's tweak it a bit more:<br/><br/>

  `test_module01.py`

  ```python
  def test_addition():
    assert 5 + 5 == 10

  def test_subtraction():
      assert 5 - 5 != 0, "Intentional failure 1"
  
  def test_integer_division():
      assert 9 // 5 == 1
  ```
  
    The output looks something like this:
    
  ```bash
  $  pytest pytest-topics
  ======================================================================= test session starts =======================================================================
  platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  collected 3 items                                                                                                                                                 
  
  pytest-topics/test_module01.py .F.                                                                                                                          [100%]
  
  ============================================================================ FAILURES =============================================================================
  ________________________________________________________________________ test_subtraction _________________________________________________________________________
  
      def test_subtraction():
  >       assert 5 - 5 != 0, "Intentional failure 1"
  E       AssertionError: Intentional failure 1
  E       assert (5 - 5) != 0
  
  pytest-topics/test_module01.py:5: AssertionError
  ===================================================================== short test summary info =====================================================================
  FAILED pytest-topics/test_module01.py::test_subtraction - AssertionError: Intentional failure 1
  =================================================================== 1 failed, 2 passed in 0.02s ===================================================================
  ```
  
- We can see that 2 test cases passed and 1 failed. The output also shows the error message that we passed in the test function.
- You can also run the same in verbose mode by running the command:
  
  ```bash
  $  pytest -v pytest-topics                                1 ✘  pythonProject   at 21:15:52  
  ======================================================================= test session starts =======================================================================
  platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python
  cachedir: .pytest_cache
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  collected 3 items                                                                                                                                                 
  
  pytest-topics/test_module01.py::test_addition PASSED                                                                                                        [ 33%]
  pytest-topics/test_module01.py::test_subtraction FAILED                                                                                                     [ 66%]
  pytest-topics/test_module01.py::test_integer_division PASSED                                                                                                [100%]
  
  ============================================================================ FAILURES =============================================================================
  ________________________________________________________________________ test_subtraction _________________________________________________________________________
  
      def test_subtraction():
  >       assert 5 - 5 != 0, "Intentional failure 1"
  E       AssertionError: Intentional failure 1
  E       assert (5 - 5) != 0
  
  pytest-topics/test_module01.py:5: AssertionError
  ===================================================================== short test summary info =====================================================================
  FAILED pytest-topics/test_module01.py::test_subtraction - AssertionError: Intentional failure 1
  =================================================================== 1 failed, 2 passed in 0.01s ===================================================================
  ```

- Here, it clearly specifies which test passed and which failed. test_subtraction failed with the error message that we passed.
- Also, the test classes should be named in the following way:
  
  ```python
  class TestModuleName:
      def test_function_name():
          pass
  ```
  
> [!IMPORTANT]
> The file name should follow the naming convention `test_something.py` and the test function should follow the naming convention `test_function_name()`.
> On, the similar note the test class should follow the naming convention `class TestClassName:` followed by the test functions conventions mentioned before.


> [!TIP]
> It's always better to have everything as a python package. All the python packages will have `__init__.py` file in them. This will help in importing the modules easily.
> <br/><br/> Whenever you create a python folder, it's always better to create this file as well within your python folders.

<hr/>

## Running Our Tests

- So, far we have been using the terminal to run the pytest commands. We can also do the same using the Pycharm IDE.
- Go to settings, and search for `test` keyword in the search bar.<br/><br/>
  
  ![](./imgs/Screenshot%202025-02-19%20at%209.31.43%E2%80%AFPM.png)

- You will see `Python Integrated Tools` in the search results in the `tools` section. Click on it.<br/><br/>
  
  ![](./imgs/Screenshot%202025-02-19%20at%209.32.32%E2%80%AFPM.png)

- Click on the dropdown for `Default test runner` and select `pytest` from the dropdown.<br/><br/>
- Now, bring your cursor on the first line of the file and right-click. You will see an option to run the test.<br/><br/>
  
  ![](./imgs/Screenshot%202025-02-19%20at%209.35.28%E2%80%AFPM.png)<br/><br/>

- Click on the `Run 'pytest in test_module01'` option. You will see logs like this:<br/><br/>

  ```bash
  /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python /Users/akd/Applications/PyCharm Community Edition.app/Contents/plugins/python-ce/helpers/pycharm/_jb_pytest_runner.py --path /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/pytest-topics/test_module01.py 
  Testing started at 9:43 pm ...
  Launching pytest with arguments /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/pytest-topics/test_module01.py --no-header --no-summary -q in /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/pytest-topics
  
  ============================= test session starts ==============================
  collecting ... collected 3 items
  
  test_module01.py::test_addition PASSED                                   [ 33%]
  test_module01.py::test_subtraction FAILED                                [ 66%]
  test_module01.py:4 (test_subtraction)
  0 != 0
  
  Expected :0
  Actual   :0
  <Click to see difference>
  
  def test_subtraction():
  >       assert 5 - 5 != 0, "Intentional failure 1"
  E       AssertionError: Intentional failure 1
  E       assert (5 - 5) != 0
  
  test_module01.py:6: AssertionError
  
  test_module01.py::test_integer_division PASSED                           [100%]
  
  ========================= 1 failed, 2 passed in 0.01s ==========================
  
  Process finished with exit code 1
  ```
  
  ![](./imgs/Screenshot%202025-02-19%20at%209.46.47%E2%80%AFPM.png)

<hr/>

## Understanding Test Output

- So, for now we will consider the recent test output generated by using the command `pytest -v pytest-topics`.<br/><br/>

  ```bash
  $ pytest -v pytest-topics
  ================================================================== test session starts ==================================================================
  platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python
  cachedir: .pytest_cache
  rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
  collected 3 items                                                                                                                                       
  
  pytest-topics/test_module01.py::test_addition PASSED                                                                                              [ 33%]
  pytest-topics/test_module01.py::test_subtraction FAILED                                                                                           [ 66%]
  pytest-topics/test_module01.py::test_integer_division PASSED                                                                                      [100%]
  
  ======================================================================= FAILURES ========================================================================
  ___________________________________________________________________ test_subtraction ____________________________________________________________________
  
      def test_subtraction():
  >       assert 5 - 5 != 0, "Intentional failure 1"
  E       AssertionError: Intentional failure 1
  E       assert (5 - 5) != 0
  
  pytest-topics/test_module01.py:6: AssertionError
  ================================================================ short test summary info ================================================================
  FAILED pytest-topics/test_module01.py::test_subtraction - AssertionError: Intentional failure 1
  ============================================================== 1 failed, 2 passed in 0.01s ==============================================================
  ```

- In the 1<sup>st</sup> line, it shows start of the test session in a well formatted way as shown above.
- The 2<sup>nd</sup> line shows the platform on which the test is running, the python version, the pytest version and the pluggy version, followed by the path to the python executable.
- Next, it shows the cache directory as `.pytest_cache`
- Next, is the root directory of the project, where we have tests within this directory.
- And, then you see the collected test items, which in our case is 3.
- Then, it shows all the test cases run from each file, and the status of the test case.
- Post, that we have a failure section, which shows the failed test case and the error message. It clearly shows the cause of the failure.
- At the end, we have a short test summary info, which shows the number of tests failed and passed.

<hr/>

## `.pytest_cache`

- The `.pytest_cache` directory is created by `pytest` to store the cache of the test results.
- It stores the information about the last run of the test results.
- We have 2 flags that we can use to control the cache:
  - `-ff` or `--failed-first` - This flag will run the failed tests first.
  - `-lf` or `--last-failed` - This flag will run the failed tests from the last run only.
  - `-nf` or `--new-first` - This flag will run the new tests first.
  - `--cache-clear` - This flag will clear the cache.
  - `--cache-show` - This flag will show the cache.

  - If, you want to see this do:

    ```bash
    $ cd .pytest_cache
    $ tree
    .
    ├── CACHEDIR.TAG
    ├── README.md
    └── v
        └── cache
            ├── lastfailed
            ├── nodeids
            └── stepwise
    3 directories, 5 files
    $ cd v/cache
    $ cat lastfailed
      {
        "pytest/test_module01.py": true,
        "pytest-topics/test_module01.py::test_false": true,
        "pytest-topics/test_module01.py::test_subtraction": true
      }%     
    ```