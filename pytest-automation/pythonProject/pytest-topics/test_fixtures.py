import pytest

class TestCases:

    @pytest.fixture()
    def setup_city(self):
        print("Fixture under execution.")
        city = ['Singapore','Delhi','Chicago','Almaty']
        return city # It's not mandatory, that a fixture must always return something.

    def test_city(self, setup_city):
        try:
            print(setup_city)
            assert setup_city[0]  == 'Singapore'
            assert setup_city[::2] == ['Singapore', 'Chicago']

        except Exception as e:
            print(f"Unknown Error Occured {e}")

    def reverse_str_array(self, lst):
        lst.reverse()
        return lst

    def test_city_reversed(self,setup_city):
        try:
            r =  self.reverse_str_array(setup_city)
            print(f"\nReversed Values for the setup_city: {r}")
            assert setup_city[::-1] == self.reverse_str_array(setup_city)
        except Exception as e:
            print(f"Unknown Error Occured {e}")



if __name__ == '__main__':
    test = TestCases()
    test.test_city()