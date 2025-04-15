import pytest

class TestCases:

    def test_readCmdOpt(self,cmdOpt):
        print(f"Reading the config file: {cmdOpt.readline()}")