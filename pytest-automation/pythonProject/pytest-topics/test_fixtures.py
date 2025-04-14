import pytest

days_1 = ['mon', 'tue', 'wed']
days_2 = ['fri', 'sat', 'sun']
filename = "file1.txt"

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

    @pytest.fixture()
    def days_2_manipulation(self):
        wk = days_2.copy()
        wk.insert(0,'thur')
        yield wk
        print("days_2 manipulation over.")

    def test_equalLength(self,teardown_setup,days_2_manipulation):
        try:
            assert len(days_1 + days_2_manipulation) == len(teardown_setup + days_2)
        except Exception as e:
            print(f"Unexpected Error Occurred: {e}")

    @pytest.fixture()
    def file_write(self):
        f = open(filename, 'w')
        print("File Written with Data.")
        f.write("Pytest is good.")
        f.close()
        f = open(filename, 'r+')
        yield f
        print("\n File Available for reading")

    def test_fileData(self, file_write):
        try:
            assert (file_write.readline()) == "Pytest is good."
        except Exception as e:
            print(f"Unknown error occured {e}.")


if __name__ == '__main__':
    test = TestCases()