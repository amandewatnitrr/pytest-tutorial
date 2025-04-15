import pytest
import math

dataset = [
    ((1,2,3), 'sum', 6),
    ((2,3,4), 'sum', 9),
    ((2,3,4), 'prod', 24)
]

dataset1 = [(1,2),(3,4),(5,6),(7,8),(10,9)]


class TestCase:

    @pytest.mark.parametrize("a,b", dataset1)
    def test_greater(self, a, b):
        assert b > a, f"{b} is not greater than {a}"

    @pytest.mark.parametrize("a,b,c",dataset)
    def test_solutions(self,a,b,c):
        try:
            if b == "sum":
                assert sum(a) == c
            elif b == "prod":
                assert math.prod(a) == c
        except Exception as e:
            print("Wrong Operation Value Assigned")

    def run_tests(self):
        try:
            for a,b,c in dataset:
                self.test_solutions(a,b,c)
        except Exception as e:
            print("Unknown Error Occurred.")


if __name__ == '__main__':
    test = TestCase()
    test.run_tests()
