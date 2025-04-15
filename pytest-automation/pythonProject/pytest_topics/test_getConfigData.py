import pytest
from pytest_topics.utils.configParserOOP import ConfigParser

config  = ConfigParser('prod.ini')
class TestCases():

    def test_getGmailUrl_qa(self):
        assert config.getGmailUrl() == 'qa.gmail.com'

    def test_getGmailUrl_prod(self):
        assert config.getGmailUrl() == 'qa_prod.gmail.com'




if __name__ == '__main__':
    test = TestCases()