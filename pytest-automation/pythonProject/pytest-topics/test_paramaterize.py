import pytest

dataset = [(1,2),(3,4),(5,6),(7,8),(10,9)]

class TestCase:

    @pytest.mark.parametrize("a,b", dataset)
    def test_greater(self, a, b):
        assert b > a, f"{b} is not greater than {a}"

    def run_tests(self):
        for a,b in dataset:
            print(f"Running for a={a} and b={b}")
            self.test_greater(a,b)

if __name__ == '__main__':
    test = TestCase()
    test.run_tests()
