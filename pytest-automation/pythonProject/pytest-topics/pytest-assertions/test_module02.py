

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