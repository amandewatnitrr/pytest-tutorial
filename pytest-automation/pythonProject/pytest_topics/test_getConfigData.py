import pytest
from pytest_topics.utils.myconfigparser import *

class TestCases:

    def test_getGmailUrl(self):
        try:
            print(f"Gmail URL: {getGmailUrl()}")
            assert getGmailUrl() == 'qa.gmail.com'
        except Exception as e:
            print(f"Unknown Error Occured: {e}.")



if __name__ == '__main__':
    test = TestCases()