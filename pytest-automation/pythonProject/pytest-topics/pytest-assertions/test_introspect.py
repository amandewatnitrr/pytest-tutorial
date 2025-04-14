import pytest

digits = [1,2,3,4,5,6,7,8,9,0]

class Testcases:

    def test_addition(self,function_detail):
        assert 1 + 1 == 2

    def test_factory(self,return_tuple_or_list):
        assert type(return_tuple_or_list('tuple')) == tuple
        assert type(return_tuple_or_list('list')) == list


if __name__ == '__main__':
    test = Testcases()
