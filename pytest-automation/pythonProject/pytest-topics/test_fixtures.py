import pytest

days_1 = ['mon', 'tue', 'wed']
days_2 = ['fri', 'sat', 'sun']

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


    @pytest.mark.usefixtures("setup_city")
    def test_alwaysTure(self):
        assert 1==1

    @pytest.mark.xfail(reason="usefixture decorator cannot use the return value coming from the Fixture.")
    @pytest.mark.usefixtures("setup_city")
    def test_fixtureAccessUsingMark(self):
        assert setup_city[0] == 'Singapore'

    @pytest.fixture()
    def teardown_setup(self):
        wk = days_1.copy()
        wk.append('thur')
        yield wk

        # Teardown started
        print("\n Week Completed - Teardown Started")
        wk.pop()
        print("Teardown Ended")

    def test_completeWeek(self, teardown_setup):
        teardown_setup.extend(days_2)
        try:
            assert teardown_setup == ['mon', 'tue', 'wed', 'thur','fri', 'sat', 'sun']
        except Exception as e:
            print(f"Error Occured: {e}.")


if __name__ == '__main__':
    test = TestCases()