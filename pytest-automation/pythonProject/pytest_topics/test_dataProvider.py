import pytest
from pytest_topics.utils.utils import get_data

class TestCases:

    @pytest.mark.parametrize("a,b,c,d",get_data())
    def test_checkFileData(self,a,b,c,d):
        print(f"{b}'s  age is {a}.")
