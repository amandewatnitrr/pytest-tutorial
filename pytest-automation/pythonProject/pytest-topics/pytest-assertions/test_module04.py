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