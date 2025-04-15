
import pytest
import re
import requests

testset = [(1,2),(2,1)]

def func1():
    raise ValueError("Exception func1")

class TestCases:
    def test_zero_divisibility(self):
        with pytest.raises(Exception):
            assert (1/0)

    @pytest.mark.parametrize("a, b", testset)
    def test_equation(self,a,b):
        summ = a+b
        diff = a-b
        asq = a*a
        bsq = b*b
        lhs = summ * diff
        rhs = asq - bsq
        assert lhs == rhs

    def test_404(self):
        with pytest.raises(Exception):
            assert requests.get("https://httpbin.org/status/404"), f"404 Response Code"

    def test_error_assert(self):
        with pytest.raises(Exception) as e:
            func1()
        print(str(e))
        assert (str(e.value)) == "Exception func1"

    def test_tuple_cmpr(self):
        with pytest.raises(Exception) as e:
            assert (1,2,3) == (1,2,4)

    def run_tests(self):
        self.test_zero_divisibility()
        self.test_404()
        self.test_tuple_cmpr()


        for a,b in testset:
            try:
                self.test_equation(a,b)
            except AssertionError as e:
                print(f"AssertionError: {e}")

if __name__ == '__main__':
    test = TestCases()
    test.run_tests()