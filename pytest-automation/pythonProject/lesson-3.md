# Pytest: Skip/Mark and Pytest Options

## Skipping pytests

- In order to skip a test, we can do it using:

  ```python
  @pytest.mark.skip(reason="Skipping Test")
  # Test case to be skipped
  def test_testing():
      pass
  ```
  
- Let's understand this through an example:

	```python
	import pytest
	
	# Corrected testset (fixed last entry and added missing Celsius value)
	cent = [8, 42, 100, 23, 35]
	faren = [46.4, 107.6, 212.0, 73.4, 95.0]
	CONVERSION_CONST = 9/5  # Constants in uppercase
	testset = zip(cent,faren)
	
	class TestCases:
	
	    @staticmethod
	    def cent_to_faren(cent=0):
	        """Static method for conversion"""
	        return (cent * CONVERSION_CONST) + 32
	
	    @pytest.mark.parametrize("cent,expected", zip(cent, faren))
	    def test_conversion(self, cent, expected):
	        """Test conversion with various values"""
	        result = self.cent_to_faren(cent)
	        # Use pytest.approx for floating point comparisons
	        assert result == pytest.approx(expected, rel=1e-3)
	
	    def test_no_input(self):
	        """Test default parameter value"""
	        assert self.cent_to_faren() == 32
	
	    @pytest.mark.skip(reason="Skipping Test")
	    @pytest.mark.parametrize("temperature", cent)
	    def test_datatype_confirm_float(self, temperature):
	        """Test return type is float"""
	        result = self.cent_to_faren(temperature)
	        assert type(result) == float
	
	    def run_tests(self):
	
	        self.test_no_input()
	        for a,b in testset:
	            self.test_conversion(a,b)
	
	if __name__ == '__main__':
	    # Run pytest programmatically (no need for custom test runner)
	    test = TestCases()
	    test.run_tests()
	```
 
    So, here you see that we have written some nice test cases. The `test_datatype_confirm_float` function will never run, as it is marked to be skipped all the times.
	Once, you run the `pytest` command, we get the following input.

	```python
	$ pytest -v ./pytest-topics/pytest-assertions/test_module04.py 
	=============================================================== test session starts ================================================================
	platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python
	cachedir: .pytest_cache
	rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
	collected 11 items                                                                                                                                 
	
	pytest-topics/pytest-assertions/test_module04.py::TestCases::test_conversion[8-46.4] PASSED                                                  [  9%]
	pytest-topics/pytest-assertions/test_module04.py::TestCases::test_conversion[42-107.6] PASSED                                                [ 18%]
	pytest-topics/pytest-assertions/test_module04.py::TestCases::test_conversion[100-212.0] PASSED                                               [ 27%]
	pytest-topics/pytest-assertions/test_module04.py::TestCases::test_conversion[23-73.4] PASSED                                                 [ 36%]
	pytest-topics/pytest-assertions/test_module04.py::TestCases::test_conversion[35-95.0] PASSED                                                 [ 45%]
	pytest-topics/pytest-assertions/test_module04.py::TestCases::test_no_input PASSED                                                            [ 54%]
	pytest-topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[8] SKIPPED (Skipping Test)                          [ 63%]
	pytest-topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[42] SKIPPED (Skipping Test)                         [ 72%]
	pytest-topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[100] SKIPPED (Skipping Test)                        [ 81%]
	pytest-topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[23] SKIPPED (Skipping Test)                         [ 90%]
	pytest-topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[35] SKIPPED (Skipping Test)                         [100%]
	
	=========================================================== 6 passed, 5 skipped in 0.01s ===========================================================
	```
 
- The another type of skip is a conditional skip, where in a test is skipped based on a certain condition:

  ```python
  @pytest.mark.skipif(logic,reason="<reason__statement")
  ```

- Let's try to undertsand this with an example:

    ```python
	import sys
	import pytest
	import requests
	
	# Corrected testset (fixed last entry and added missing Celsius value)
	cent = [8, 42, 100, 23, 35]
	faren = [46.4, 107.6, 212.0, 73.4, 95.0]
	CONVERSION_CONST = 9/5  # Constants in uppercase
	testset = zip(cent,faren)
	
	class TestCases:
	
	    @staticmethod
	    def cent_to_faren(cent=0):
	        """Static method for conversion"""
	        return (cent * CONVERSION_CONST) + 32
	
	    @pytest.mark.parametrize("cent,expected", zip(cent, faren))
	    def test_conversion(self, cent, expected):
	        """Test conversion with various values"""
	        result = self.cent_to_faren(cent)
	        # Use pytest.approx for floating point comparisons
	        assert result == pytest.approx(expected, rel=1e-3)
	
	    def test_no_input(self):
	        """Test default parameter value"""
	        assert self.cent_to_faren() == 32
	
	    @pytest.mark.skip(reason="Skipping Test")
	    @pytest.mark.parametrize("temperature", cent)
	    def test_datatype_confirm_float(self, temperature):
	        """Test return type is float"""
	        result = self.cent_to_faren(temperature)
	        assert type(result) == float
	
	    @pytest.mark.skipif(sys.version_info > (3,6),reason="Don't execute this for python version above 3.8")
	    def test_404(self):
	        with pytest.raises(Exception):
	            assert requests.get("https://httpbin.org/status/404"), f"404 Response Code"
	
	    def run_tests(self):
	
	        self.test_no_input()
	        for a,b in testset:
	            self.test_conversion(a,b)
	
	if __name__ == '__main__':
	    # Run pytest programmatically (no need for custom test runner)
	    test = TestCases()
	    test.run_tests()
    ```
  
	Now, if we run the `pytest` command, and exectue the test, we get the following output:

	```bash
    $ pytest -v ./pytest_topics/pytest-assertions/test_module04.py
	=============================================================== test session starts ================================================================
	platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python
	cachedir: .pytest_cache
	rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
	collected 12 items                                                                                                                                 
	
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_conversion[8-46.4] PASSED                                                  [  8%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_conversion[42-107.6] PASSED                                                [ 16%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_conversion[100-212.0] PASSED                                               [ 25%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_conversion[23-73.4] PASSED                                                 [ 33%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_conversion[35-95.0] PASSED                                                 [ 41%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_no_input PASSED                                                            [ 50%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[8] SKIPPED (Skipping Test)                          [ 58%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[42] SKIPPED (Skipping Test)                         [ 66%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[100] SKIPPED (Skipping Test)                        [ 75%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[23] SKIPPED (Skipping Test)                         [ 83%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[35] SKIPPED (Skipping Test)                         [ 91%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_404 SKIPPED (Don't execute this for python version above 3.8)              [100%]
	
	=========================================================== 6 passed, 6 skipped in 0.04s ===========================================================
	```
  
	And, in the output it clearly mentions the reason for skipping, that we mentioned in the argument of `@python.mark.skipif()`.

## Markers in Pytest

- Pytest provides a way to mark tests with certain attributes, which can be used to filter tests based on these attributes.
- We can mark tests with `@pytest.mark.<marker_name>` and then use these markers to filter tests.
  
  ```python
  @pytest.mark.<marker_name>
  def test_testing():
	  pass
  ```
  
  And, can be run using the following command:
  
  ```bash
  $ pytest -m <marker_name>
  ```
  
- A test can have multiple markers, and the same marker can be used on multiple tests.
  - Let's understand this through an example:

      ```python
      import sys
      import pytest
      import requests
	
      # Corrected testset (fixed last entry and added missing Celsius value)
      cent = [8, 42, 100, 23, 35]
      faren = [46.4, 107.6, 212.0, 73.4, 95.0]
      CONVERSION_CONST = 9/5  # Constants in uppercase
      testset = zip(cent,faren)
	
      class TestCases:
	
          @staticmethod
          def cent_to_faren(cent=0):
              """Static method for conversion"""
              return (cent * CONVERSION_CONST) + 32
	
          @pytest.mark.temp_conversion
          @pytest.mark.parametrize("cent,expected", zip(cent, faren))
          def test_conversion(self, cent, expected):
              """Test conversion with various values"""
              result = self.cent_to_faren(cent)
              # Use pytest.approx for floating point comparisons
              assert result == pytest.approx(expected, rel=1e-3)
	
          @pytest.mark.temp_conversion
          def test_no_input(self):
              """Test default parameter value"""
              assert self.cent_to_faren() == 32
	
          @pytest.mark.skip(reason="Skipping Test")
          @pytest.mark.parametrize("temperature", cent)
          def test_datatype_confirm_float(self, temperature):
              """Test return type is float"""
              result = self.cent_to_faren(temperature)
              assert type(result) == float
	
          @pytest.mark.skipif(sys.version_info > (3,6),reason="Don't execute this for python version above 3.8")
          def test_404(self):
              with pytest.raises(Exception):
                  assert requests.get("https://httpbin.org/status/404"), f"404 Response Code"
	
          def test_str_slice(self):
              letters = 'abcdefghijklmnopqrstuvwxyz'
              assert letters[:3] == 'abc'
              assert letters[-3:] == 'xyz'
              assert letters[:21:5] == 'afkpu'
              assert letters[::-1] == 'zyxwvutsrqponmlkjihgfedcba'
	
          def test_str_split(self):
              s = "My name is Aman and, I am a Python Developer"
              assert s.split() == ['My', 'name', 'is', 'Aman', 'and,', 'I', 'am', 'a', 'Python', 'Developer']
              assert s.split(',') == ['My name is Aman and', ' I am a Python Developer']
	
          def run_tests(self):
	
              self.test_no_input()
              for a,b in testset:
                  self.test_conversion(a,b)
	
      if __name__ == '__main__':
          # Run pytest programmatically (no need for custom test runner)
          test = TestCases()
          test.run_tests()
      ```
 
      Now, run the following command to all specifically marked tests:
 
      ```bash
      $ pytest -v -m temp_conversion
      ```
 
      And, then analyse the output:

      ```bash
      $  pytest -v -m 'temp_conversion' 
      =============================================================== test session starts ================================================================
      platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python
      cachedir: .pytest_cache
      rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
      collected 47 items / 41 deselected / 6 selected                                                                                                    
	
      pytest_topics/test_marker_skip.py::TestCases::test_conversion[8-46.4] PASSED                                                                 [ 16%]
      pytest_topics/test_marker_skip.py::TestCases::test_conversion[42-107.6] PASSED                                                               [ 33%]
      pytest_topics/test_marker_skip.py::TestCases::test_conversion[100-212.0] PASSED                                                              [ 50%]
      pytest_topics/test_marker_skip.py::TestCases::test_conversion[23-73.4] PASSED                                                                [ 66%]
      pytest_topics/test_marker_skip.py::TestCases::test_conversion[35-95.0] PASSED                                                                [ 83%]
      pytest_topics/test_marker_skip.py::TestCases::test_no_input PASSED                                                                           [100%]
	
      ================================================================= warnings summary =================================================================
      pytest_topics/test_marker_skip.py:19
      /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/pytest_topics/test_marker_skip.py:19: PytestUnknownMarkWarning: Unknown pytest.mark.temp_conversion - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
      @pytest.mark.temp_conversion
	
      pytest_topics/test_marker_skip.py:27
      /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/pytest_topics/test_marker_skip.py:27: PytestUnknownMarkWarning: Unknown pytest.mark.temp_conversion - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
      @pytest.mark.temp_conversion
	
      -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
      =================================================== 6 passed, 41 deselected, 2 warnings in 0.04s ===================================================
      ```
    
	You can clearly see, that only the tests marked with `@pytest.mark.temp_conversion` are executed. And, no other tests are executed.

### Running Multiple Marked Tests

- Now, once we know how to run marked tests, let's see how to run multiple marked tests.
- We can avoid running certain marked test cases using the command:

  ```bash
  $ pytest -v -m "not <marker_name>"
  ```

- If you want to run a certain mark but avoid running another, you can use the following command:

  ```bash
  $ pytest -v -m "<marker_name> and not <another_marker_name>"
  ```
  
- We can also run two different marked tests using the following command:

  ```bash
  $ pytest -v -m "<marker_name> or <another_marker_name>"
  ```

- We can run all the marked tests using the following command:

  ```bash
  $ pytest -v -m "<marker_name> or <another_marker_name> or <another_marker_name>"
  ```
  
- If you want to run a single test case marked by multiple markers, you can use the following command:

  ```bash
  $ pytest -v -m "<marker_name> and <another_marker_name>"
  ```
  
- If you want to run test cases, marked with multiple markers and other with single marker, you can use the following command:

  ```bash
  $ pytest -v -m "<marker_name> and <another_marker_name> or <another_marker_name>"
  ```
  
### Module Level Markers and Disable Warnings

- We can also mark the entire module with a marker, and then run the tests based on the module level marker.
- We can mark the module using the following syntax. This must be done at the top of the file:

  ```python
  pytestmark = [pytest.mark.<marker_name>, pytest.mark.<another_marker_name>,...]
  ```
  
- Let's learn this through this example:

	```python
	import sys
	import pytest
	import requests
	
	pytestmark = [pytest.mark.markerr,pytest.mark.temp_conversion, pytest.mark.str_test]
	
	# Corrected testset (fixed last entry and added missing Celsius value)
	cent = [8, 42, 100, 23, 35]
	faren = [46.4, 107.6, 212.0, 73.4, 95.0]
	CONVERSION_CONST = 9/5  # Constants in uppercase
	testset = zip(cent,faren)
	
	class TestCases:
	
	    @staticmethod
	    def cent_to_faren(cent=0):
	        """Static method for conversion"""
	        return (cent * CONVERSION_CONST) + 32
	
	    @pytest.mark.temp_conversion
	    @pytest.mark.parametrize("cent,expected", zip(cent, faren))
	    def test_conversion(self, cent, expected):
	        """Test conversion with various values"""
	        result = self.cent_to_faren(cent)
	        # Use pytest.approx for floating point comparisons
	        assert result == pytest.approx(expected, rel=1e-3)
	
	    @pytest.mark.temp_conversion
	    def test_no_input(self):
	        """Test default parameter value"""
	        assert self.cent_to_faren() == 32
	
	    @pytest.mark.skip(reason="Skipping Test")
	    @pytest.mark.parametrize("temperature", cent)
	    def test_datatype_confirm_float(self, temperature):
	        """Test return type is float"""
	        result = self.cent_to_faren(temperature)
	        assert type(result) == float
	
	    @pytest.mark.skipif(sys.version_info > (3,6),reason="Don't execute this for python version above 3.8")
	    def test_404(self):
	        with pytest.raises(Exception):
	            assert requests.get("https://httpbin.org/status/404"), f"404 Response Code"
	
	    @pytest.mark.str_test
	    def test_str_slice(self):
	        letters = 'abcdefghijklmnopqrstuvwxyz'
	        assert letters[:3] == 'abc'
	        assert letters[-3:] == 'xyz'
	        assert letters[:21:5] == 'afkpu'
	        assert letters[::-1] == 'zyxwvutsrqponmlkjihgfedcba'
	
	    @pytest.mark.str_test
	    def test_str_split(self):
	        s = "My name is Aman and, I am a Python Developer"
	        assert s.split() == ['My', 'name', 'is', 'Aman', 'and,', 'I', 'am', 'a', 'Python', 'Developer']
	        assert s.split(',') == ['My name is Aman and', ' I am a Python Developer']
	
	    def run_tests(self):
	
	        self.test_no_input()
	        self.test_404()
	        self.test_str_slice()
	        self.test_str_split()
	        for a,b in testset:
	            self.test_conversion(a,b)
	
	if __name__ == '__main__':
	    # Run pytest programmatically (no need for custom test runner)
	    test = TestCases()
	    test.run_tests()
	```
 
	Now, run the following command:

	```bash
 	$ pytest -v -m markerr
	```
 
	This will run the whole module, as it is marked with `@pytest.mark.markerr`. And, below is the output:

	```bash
	$ pytest -v -m markerr                            ✔  pythonProject   at 23:00:21  
	=============================================================== test session starts ================================================================
	platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python
	cachedir: .pytest_cache
	rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
	collected 47 items / 33 deselected / 14 selected                                                                                                   
	
	pytest_topics/test_marker_skip.py::TestCases::test_conversion[8-46.4] PASSED                                                                 [  7%]
	pytest_topics/test_marker_skip.py::TestCases::test_conversion[42-107.6] PASSED                                                               [ 14%]
	pytest_topics/test_marker_skip.py::TestCases::test_conversion[100-212.0] PASSED                                                              [ 21%]
	pytest_topics/test_marker_skip.py::TestCases::test_conversion[23-73.4] PASSED                                                                [ 28%]
	pytest_topics/test_marker_skip.py::TestCases::test_conversion[35-95.0] PASSED                                                                [ 35%]
	pytest_topics/test_marker_skip.py::TestCases::test_no_input PASSED                                                                           [ 42%]
	pytest_topics/test_marker_skip.py::TestCases::test_datatype_confirm_float[8] SKIPPED (Skipping Test)                                         [ 50%]
	pytest_topics/test_marker_skip.py::TestCases::test_datatype_confirm_float[42] SKIPPED (Skipping Test)                                        [ 57%]
	pytest_topics/test_marker_skip.py::TestCases::test_datatype_confirm_float[100] SKIPPED (Skipping Test)                                       [ 64%]
	pytest_topics/test_marker_skip.py::TestCases::test_datatype_confirm_float[23] SKIPPED (Skipping Test)                                        [ 71%]
	pytest_topics/test_marker_skip.py::TestCases::test_datatype_confirm_float[35] SKIPPED (Skipping Test)                                        [ 78%]
	pytest_topics/test_marker_skip.py::TestCases::test_404 SKIPPED (Don't execute this for python version above 3.8)                             [ 85%]
	pytest_topics/test_marker_skip.py::TestCases::test_str_slice PASSED                                                                          [ 92%]
	pytest_topics/test_marker_skip.py::TestCases::test_str_split PASSED                                                                          [100%]
	
	================================================================= warnings summary =================================================================
	pytest_topics/pytest-assertions/test_module02.py:15
	  /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/pytest_topics/pytest-assertions/test_module02.py:15: PytestUnknownMarkWarning: Unknown pytest.mark.str_test - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
	    @pytest.mark.str_test
	
	pytest_topics/pytest-assertions/test_module02.py:23
	  /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/pytest_topics/pytest-assertions/test_module02.py:23: PytestUnknownMarkWarning: Unknown pytest.mark.str_test - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
	    @pytest.mark.str_test
	
	pytest_topics/pytest-assertions/test_module02.py:27
	  /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/pytest_topics/pytest-assertions/test_module02.py:27: PytestUnknownMarkWarning: Unknown pytest.mark.str_test - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
	    @pytest.mark.str_test
	
	pytest_topics/test_marker_skip.py:5
	  /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/pytest_topics/test_marker_skip.py:5: PytestUnknownMarkWarning: Unknown pytest.mark.markerr - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
	    pytestmark = [pytest.mark.markerr,pytest.mark.temp_conversion, pytest.mark.str_test]
	
	pytest_topics/test_marker_skip.py:5
	  /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/pytest_topics/test_marker_skip.py:5: PytestUnknownMarkWarning: Unknown pytest.mark.temp_conversion - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
	    pytestmark = [pytest.mark.markerr,pytest.mark.temp_conversion, pytest.mark.str_test]
	
	pytest_topics/test_marker_skip.py:5
	  /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/pytest_topics/test_marker_skip.py:5: PytestUnknownMarkWarning: Unknown pytest.mark.str_test - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
	    pytestmark = [pytest.mark.markerr,pytest.mark.temp_conversion, pytest.mark.str_test]
	
	pytest_topics/test_marker_skip.py:20
	  /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/pytest_topics/test_marker_skip.py:20: PytestUnknownMarkWarning: Unknown pytest.mark.temp_conversion - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
	    @pytest.mark.temp_conversion
	
	pytest_topics/test_marker_skip.py:28
	  /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/pytest_topics/test_marker_skip.py:28: PytestUnknownMarkWarning: Unknown pytest.mark.temp_conversion - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
	    @pytest.mark.temp_conversion
	
	pytest_topics/test_marker_skip.py:45
	  /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/pytest_topics/test_marker_skip.py:45: PytestUnknownMarkWarning: Unknown pytest.mark.str_test - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
	    @pytest.mark.str_test
	
	pytest_topics/test_marker_skip.py:53
	  /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/pytest_topics/test_marker_skip.py:53: PytestUnknownMarkWarning: Unknown pytest.mark.str_test - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
	    @pytest.mark.str_test
	
	-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
	============================================= 8 passed, 6 skipped, 33 deselected, 10 warnings in 0.07s ==============================================
    ```

#### Disabling Warnings

- Now, in the above output, you can see that there are some warnings, which are not useful for us.
- This is happening because the markers are not defined in the pytest config file.
- So, we can disable it by creating a file named `pytest.ini` in the root directory of the project.
- And, then add the following content to the file:

  ```ini
  [pytest]
  markers =
	  temp_conversion: Test cases for temperature conversion
	  str_test: Test cases for string slicing and splitting
	  markerr: Test cases for Marker Tutorial
  ```

- Now, if we run the same command:

  ```bash
  $ pytest -v -m markerr
  ```
  
  The output will be:

    ```bash
  	$ pytest -v -m markerr 
	=============================================================== test session starts ================================================================
	platform darwin -- Python 3.11.3, pytest-7.4.2, pluggy-1.3.0 -- /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
	cachedir: .pytest_cache
	rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
	configfile: pytest.ini
	plugins: django-4.5.2
	collected 47 items / 33 deselected / 14 selected                                                                                                   
	
	pytest_topics/test_marker_skip.py::TestCases::test_conversion[8-46.4] PASSED                                                                 [  7%]
	pytest_topics/test_marker_skip.py::TestCases::test_conversion[42-107.6] PASSED                                                               [ 14%]
	pytest_topics/test_marker_skip.py::TestCases::test_conversion[100-212.0] PASSED                                                              [ 21%]
	pytest_topics/test_marker_skip.py::TestCases::test_conversion[23-73.4] PASSED                                                                [ 28%]
	pytest_topics/test_marker_skip.py::TestCases::test_conversion[35-95.0] PASSED                                                                [ 35%]
	pytest_topics/test_marker_skip.py::TestCases::test_no_input PASSED                                                                           [ 42%]
	pytest_topics/test_marker_skip.py::TestCases::test_datatype_confirm_float[8] SKIPPED (Skipping Test)                                         [ 50%]
	pytest_topics/test_marker_skip.py::TestCases::test_datatype_confirm_float[42] SKIPPED (Skipping Test)                                        [ 57%]
	pytest_topics/test_marker_skip.py::TestCases::test_datatype_confirm_float[100] SKIPPED (Skipping Test)                                       [ 64%]
	pytest_topics/test_marker_skip.py::TestCases::test_datatype_confirm_float[23] SKIPPED (Skipping Test)                                        [ 71%]
	pytest_topics/test_marker_skip.py::TestCases::test_datatype_confirm_float[35] SKIPPED (Skipping Test)                                        [ 78%]
	pytest_topics/test_marker_skip.py::TestCases::test_404 SKIPPED (Don't execute this for python version above 3.8)                             [ 85%]
	pytest_topics/test_marker_skip.py::TestCases::test_str_slice PASSED                                                                          [ 92%]
	pytest_topics/test_marker_skip.py::TestCases::test_str_split PASSED                                                                          [100%]
	
	=================================================== 8 passed, 6 skipped, 33 deselected in 0.10s ====================================================
    ```
  
  And, you can see that the warnings are not there anymore.

### xfail Markers

- Sometimes, we know that a test is going to fail, and we want to mark it as expected to fail.
- We can do this using the `@pytest.mark.xfail` decorator.
- Let's try to understand this through an example:

  For this example, we have added a test case, which is expected to fail. And, we have marked it with `@pytest.mark.xfail`.
  
    ```python
    import sys
	import pytest
	import requests
	
	# Corrected testset (fixed last entry and added missing Celsius value)
	cent = [8, 42, 100, 23, 35]
	faren = [46.4, 107.6, 212.0, 73.4, 95.0]
	CONVERSION_CONST = 9/5  # Constants in uppercase
	testset = zip(cent,faren)
	
	class TestCases:
	
	    @staticmethod
	    def cent_to_faren(cent=0):
	        """Static method for conversion"""
	        return (cent * CONVERSION_CONST) + 32
	
	    @pytest.mark.parametrize("cent,expected", zip(cent, faren))
	    def test_conversion(self, cent, expected):
	        """Test conversion with various values"""
	        result = self.cent_to_faren(cent)
	        # Use pytest.approx for floating point comparisons
	        assert result == pytest.approx(expected, rel=1e-3)
	
	    def test_no_input(self):
	        """Test default parameter value"""
	        assert self.cent_to_faren() == 32
	
	    @pytest.mark.skip(reason="Skipping Test")
	    @pytest.mark.parametrize("temperature", cent)
	    def test_datatype_confirm_float(self, temperature):
	        """Test return type is float"""
	        result = self.cent_to_faren(temperature)
	        assert type(result) == float
	
	    @pytest.mark.skipif(sys.version_info > (3,6),reason="Don't execute this for python version above 3.8")
	    def test_404(self):
	        with pytest.raises(Exception):
	            assert requests.get("https://httpbin.org/status/404"), f"404 Response Code"
	
	    @pytest.mark.xfail(reason="Expected to fail")
	    def test_404_xfail(self):
	        assert requests.get("https://httpbin.org/status/404"), f"404 Response Code"
  
  		@pytest.mark.xfail(reason="Expected to fail")		
  		def test_no_input_xpass(self):
	        """Test default parameter value"""
	        assert self.cent_to_faren() == 32
	
	    def run_tests(self):
	
	        self.test_no_input()
  	        self.test_no_input_xpass()
	        self.test_404_xfail()
	        for a,b in testset:
	            self.test_conversion(a,b)
	
	if __name__ == '__main__':
	    # Run pytest programmatically (no need for custom test runner)
	    test = TestCases()
	    test.run_tests()
    ```

- Here you can clearly see specified that test_404_xfail is expected to fail, and is marked with `@pytest.mark.xfail`.
- Now, when we run the command `pytest -v ./pytest-topics/pytest-assertions/test_module04.py`, you will get the following output:

    ```bash
    $   pytest -v ./pytest_topics/pytest-assertions/test_module04.py
	=============================================================== test session starts ================================================================
	platform darwin -- Python 3.11.3, pytest-7.4.2, pluggy-1.3.0 -- /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
	cachedir: .pytest_cache
	rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
	configfile: pytest.ini
	plugins: django-4.5.2
	collected 14 items                                                                                                                                 
	
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_conversion[8-46.4] PASSED                                                  [  7%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_conversion[42-107.6] PASSED                                                [ 14%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_conversion[100-212.0] PASSED                                               [ 21%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_conversion[23-73.4] PASSED                                                 [ 28%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_conversion[35-95.0] PASSED                                                 [ 35%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_no_input PASSED                                                            [ 42%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[8] SKIPPED (Skipping Test)                          [ 50%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[42] SKIPPED (Skipping Test)                         [ 57%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[100] SKIPPED (Skipping Test)                        [ 64%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[23] SKIPPED (Skipping Test)                         [ 71%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[35] SKIPPED (Skipping Test)                         [ 78%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_404 SKIPPED (Don't execute this for python version above 3.8)              [ 85%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_404_xfail XFAIL (Expected to fail)                                         [ 92%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_no_input_xpass XPASS (Expected to fail)                                    [100%]
	
	================================================ 6 passed, 6 skipped, 1 xfailed, 1 xpassed in 1.26s ================================================
    ```
  
  And, you can clearly see the test case that is marked to fail has actually failed, but doesn't show as failed rather as xfailed, and another test case which is supposed to fail and, marked to be failed has actually passed, but is shown as xpassed.

- xfail markers can also be used with conditions, and can be used as follows:

  ```python
  @pytest.mark.xfail(condition, reason="<reason__statement")
  ```
  
  Let's understand this with an example:

    ```python
	import sys
	
	import pytest
	import requests
	
	# Corrected testset (fixed last entry and added missing Celsius value)
	cent = [8, 42, 100, 23, 35]
	faren = [46.4, 107.6, 212.0, 73.4, 95.0]
	CONVERSION_CONST = 9/5  # Constants in uppercase
	testset = zip(cent,faren)
	
	class TestCases:
	
	    @staticmethod
	    def cent_to_faren(cent=0):
	        """Static method for conversion"""
	        return (cent * CONVERSION_CONST) + 32
	
	    @pytest.mark.parametrize("cent,expected", zip(cent, faren))
	    def test_conversion(self, cent, expected):
	        """Test conversion with various values"""
	        result = self.cent_to_faren(cent)
	        # Use pytest.approx for floating point comparisons
	        assert result == pytest.approx(expected, rel=1e-3)
	
	    def test_no_input(self):
	        """Test default parameter value"""
	        assert self.cent_to_faren() == 32
	
	    @pytest.mark.skip(reason="Skipping Test")
	    @pytest.mark.parametrize("temperature", cent)
	    def test_datatype_confirm_float(self, temperature):
	        """Test return type is float"""
	        result = self.cent_to_faren(temperature)
	        assert type(result) == float
	
	    @pytest.mark.skipif(sys.version_info > (3,6),reason="Don't execute this for python version above 3.8")
	    def test_404(self):
	        with pytest.raises(Exception):
	            assert requests.get("https://httpbin.org/status/404"), f"404 Response Code"
	
	    @pytest.mark.xfail(sys.version_info > (3,6),reason="Don't execute this for python version above 3.8")
	    def test_404_xfail(self):
	        assert requests.get("https://httpbin.org/status/404"), f"404 Response Code"
	
	    @pytest.mark.xfail(reason="Expected to fail")
	    def test_no_input_xpass(self):
	        """Test default parameter value"""
	        assert self.cent_to_faren() == 32
	
	    def run_tests(self):
	
	        self.test_no_input()
	        self.test_no_input_xpass()
	        self.test_404_xfail()
	        for a,b in testset:
	            self.test_conversion(a,b)
	
	if __name__ == '__main__':
	    # Run pytest programmatically (no need for custom test runner)
	    test = TestCases()
	    test.run_tests()  
    ```
  
- Here' in the above example, we have given a condition for xfail, that if the python version is greater than 3.6, then the test case is expected to fail.
- If you run the command `pytest -v ./pytest-topics/pytest-assertions/test_module04.py`, you will get the following output:

    ```bash
    $ pytest -v ./pytest_topics/pytest-assertions/test_module04.py
	=============================================================== test session starts ================================================================
	platform darwin -- Python 3.11.3, pytest-7.4.2, pluggy-1.3.0 -- /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
	cachedir: .pytest_cache
	rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
	configfile: pytest.ini
	plugins: django-4.5.2
	collected 14 items                                                                                                                                 
	
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_conversion[8-46.4] PASSED                                                  [  7%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_conversion[42-107.6] PASSED                                                [ 14%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_conversion[100-212.0] PASSED                                               [ 21%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_conversion[23-73.4] PASSED                                                 [ 28%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_conversion[35-95.0] PASSED                                                 [ 35%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_no_input PASSED                                                            [ 42%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[8] SKIPPED (Skipping Test)                          [ 50%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[42] SKIPPED (Skipping Test)                         [ 57%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[100] SKIPPED (Skipping Test)                        [ 64%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[23] SKIPPED (Skipping Test)                         [ 71%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[35] SKIPPED (Skipping Test)                         [ 78%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_404 SKIPPED (Don't execute this for python version above 3.8)              [ 85%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_404_xfail XFAIL (Don't execute this for python version above 3.8)          [ 92%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_no_input_xpass XPASS (Expected to fail)                                    [100%]
	
	================================================ 6 passed, 6 skipped, 1 xfailed, 1 xpassed in 1.23s ================================================
    ```

  Here, in this example you can clearly see that it specifies the reason for xfail, and also tested the marker against a condition, and the test case is marked as xfail.

## Run Pytest by Test Name

- Sometimes, we want to run a specific test case, and we don't want to run all the test cases.
- We can do this by specifying the test case name using the `-k` flag.
- Let's understand this through an example:

  Run the command: `pytest -vk 0k "module" --tb=no`. This will only run the test cases where file name contains the keyword "module" in it.

    ```bash
    $ pytest -v -k "module" --tb=no 
	=============================================================== test session starts ================================================================
	platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python
	cachedir: .pytest_cache
	rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
	configfile: pytest.ini
	collected 50 items / 15 deselected / 35 selected                                                                                                   
	
	pytest_topics/pytest-assertions/test_module02.py::TestCases::test_greater[9-5] PASSED                                                        [  2%]
	pytest_topics/pytest-assertions/test_module02.py::TestCases::test_greater[5-9] FAILED                                                        [  5%]
	pytest_topics/pytest-assertions/test_module02.py::TestCases::test_greater[5-4] PASSED                                                        [  8%]
	pytest_topics/pytest-assertions/test_module02.py::TestCases::test_greater[10-5] PASSED                                                       [ 11%]
	pytest_topics/pytest-assertions/test_module02.py::TestCases::test_true PASSED                                                                [ 14%]
	pytest_topics/pytest-assertions/test_module02.py::TestCases::test_cmpr_string_char PASSED                                                    [ 17%]
	pytest_topics/pytest-assertions/test_module02.py::TestCases::test_divmod[9-5] PASSED                                                         [ 20%]
	pytest_topics/pytest-assertions/test_module02.py::TestCases::test_divmod[5-9] FAILED                                                         [ 22%]
	pytest_topics/pytest-assertions/test_module02.py::TestCases::test_divmod[5-4] PASSED                                                         [ 25%]
	pytest_topics/pytest-assertions/test_module02.py::TestCases::test_divmod[10-5] FAILED                                                        [ 28%]
	pytest_topics/pytest-assertions/test_module02.py::TestCases::test_find_in_string PASSED                                                      [ 31%]
	pytest_topics/pytest-assertions/test_module02.py::TestCases::test_is_not_in_string PASSED                                                    [ 34%]
	pytest_topics/pytest-assertions/test_module03.py::TestCases::test_zero_divisibility PASSED                                                   [ 37%]
	pytest_topics/pytest-assertions/test_module03.py::TestCases::test_equation[1-2] PASSED                                                       [ 40%]
	pytest_topics/pytest-assertions/test_module03.py::TestCases::test_equation[2-1] PASSED                                                       [ 42%]
	pytest_topics/pytest-assertions/test_module03.py::TestCases::test_404 PASSED                                                                 [ 45%]
	pytest_topics/pytest-assertions/test_module03.py::TestCases::test_error_assert PASSED                                                        [ 48%]
	pytest_topics/pytest-assertions/test_module03.py::TestCases::test_tuple_cmpr PASSED                                                          [ 51%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_conversion[8-46.4] PASSED                                                  [ 54%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_conversion[42-107.6] PASSED                                                [ 57%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_conversion[100-212.0] PASSED                                               [ 60%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_conversion[23-73.4] PASSED                                                 [ 62%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_conversion[35-95.0] PASSED                                                 [ 65%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_no_input PASSED                                                            [ 68%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[8] SKIPPED (Skipping Test)                          [ 71%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[42] SKIPPED (Skipping Test)                         [ 74%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[100] SKIPPED (Skipping Test)                        [ 77%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[23] SKIPPED (Skipping Test)                         [ 80%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[35] SKIPPED (Skipping Test)                         [ 82%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_404 SKIPPED (Don't execute this for python version above 3.8)              [ 85%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_404_xfail XFAIL (Don't execute this for python version above 3.8)          [ 88%]
	pytest_topics/pytest-assertions/test_module04.py::TestCases::test_no_input_xpass XPASS (Expected to fail)                                    [ 91%]
	pytest_topics/test_module01.py::test_addition PASSED                                                                                         [ 94%]
	pytest_topics/test_module01.py::test_subtraction FAILED                                                                                      [ 97%]
	pytest_topics/test_module01.py::test_integer_division PASSED                                                                                 [100%]
	
	============================================================= short test summary info ==============================================================
	FAILED pytest_topics/pytest-assertions/test_module02.py::TestCases::test_greater[5-9] - AssertionError: 5 is not greater than 9
	FAILED pytest_topics/pytest-assertions/test_module02.py::TestCases::test_divmod[5-9] - AssertionError: 1 is not in divmod(5,9)
	FAILED pytest_topics/pytest-assertions/test_module02.py::TestCases::test_divmod[10-5] - AssertionError: 1 is not in divmod(10,5)
	FAILED pytest_topics/test_module01.py::test_subtraction - AssertionError: Intentional failure 1
	=================================== 4 failed, 23 passed, 6 skipped, 15 deselected, 1 xfailed, 1 xpassed in 5.85s ===================================
    ```
  
- `--tb=no` sets traceback to no, to avoid seeing all the unnecessary reason of errors. We can also run test case functions having specific keyword using the same command, here's the example:

  ```bash
  pytest -v -k "str" --tb=no 
  ```

## Pytest Cmd Line Options

- `-x` is used when we need to come out of the test case, as soon as the first test-case failure happens.
- `--maxfail=<number>` is used when we need to come out of tet case, after certain number of failures.
- `-q` is used for quiet execution when we want to decrease the verbosity of the logs generated.
- `--collect-only` or `-co` is used when you just want to collect the test cases but not exectue them.
- `--lf` or `--last-failed` is used when we want to execute only the test cases that failed during the previous run.
- `-ff` or `--failed-first` runs the test cases that failed during the previous run first, and than others.
- `--junit-xml=<path>` is used to generate a test report upon execution in xml format.
