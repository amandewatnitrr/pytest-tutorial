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