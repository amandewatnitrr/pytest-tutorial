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
    $ pytest -v ./pytest-topics/pytest-assertions/test_module04.py
	=============================================================== test session starts ================================================================
	platform darwin -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/.venv/bin/python
	cachedir: .pytest_cache
	rootdir: /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject
	collected 12 items                                                                                                                                 
	
	pytest-topics/pytest-assertions/test_module04.py::TestCases::test_conversion[8-46.4] PASSED                                                  [  8%]
	pytest-topics/pytest-assertions/test_module04.py::TestCases::test_conversion[42-107.6] PASSED                                                [ 16%]
	pytest-topics/pytest-assertions/test_module04.py::TestCases::test_conversion[100-212.0] PASSED                                               [ 25%]
	pytest-topics/pytest-assertions/test_module04.py::TestCases::test_conversion[23-73.4] PASSED                                                 [ 33%]
	pytest-topics/pytest-assertions/test_module04.py::TestCases::test_conversion[35-95.0] PASSED                                                 [ 41%]
	pytest-topics/pytest-assertions/test_module04.py::TestCases::test_no_input PASSED                                                            [ 50%]
	pytest-topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[8] SKIPPED (Skipping Test)                          [ 58%]
	pytest-topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[42] SKIPPED (Skipping Test)                         [ 66%]
	pytest-topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[100] SKIPPED (Skipping Test)                        [ 75%]
	pytest-topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[23] SKIPPED (Skipping Test)                         [ 83%]
	pytest-topics/pytest-assertions/test_module04.py::TestCases::test_datatype_confirm_float[35] SKIPPED (Skipping Test)                         [ 91%]
	pytest-topics/pytest-assertions/test_module04.py::TestCases::test_404 SKIPPED (Don't execute this for python version above 3.8)              [100%]
	
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
	
      pytest-topics/test_marker_skip.py::TestCases::test_conversion[8-46.4] PASSED                                                                 [ 16%]
      pytest-topics/test_marker_skip.py::TestCases::test_conversion[42-107.6] PASSED                                                               [ 33%]
      pytest-topics/test_marker_skip.py::TestCases::test_conversion[100-212.0] PASSED                                                              [ 50%]
      pytest-topics/test_marker_skip.py::TestCases::test_conversion[23-73.4] PASSED                                                                [ 66%]
      pytest-topics/test_marker_skip.py::TestCases::test_conversion[35-95.0] PASSED                                                                [ 83%]
      pytest-topics/test_marker_skip.py::TestCases::test_no_input PASSED                                                                           [100%]
	
      ================================================================= warnings summary =================================================================
      pytest-topics/test_marker_skip.py:19
      /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/pytest-topics/test_marker_skip.py:19: PytestUnknownMarkWarning: Unknown pytest.mark.temp_conversion - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
      @pytest.mark.temp_conversion
	
      pytest-topics/test_marker_skip.py:27
      /Users/akd/Github/pytest-tutorial/pytest-automation/pythonProject/pytest-topics/test_marker_skip.py:27: PytestUnknownMarkWarning: Unknown pytest.mark.temp_conversion - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
      @pytest.mark.temp_conversion
	
      -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
      =================================================== 6 passed, 41 deselected, 2 warnings in 0.04s ===================================================
      ```
    
	You can clearly see, that only the tests marked with `@pytest.mark.temp_conversion` are executed. And, no other tests are executed.