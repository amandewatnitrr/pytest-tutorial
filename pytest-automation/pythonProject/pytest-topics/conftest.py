import pytest
import os

def pytest_configure():
    pytest.days_1 = ['mon', 'tue', 'wed']
    pytest.days_2 = ['fri', 'sat', 'sun']


@pytest.fixture()
def setup_city():
    print("Fixture under execution.")
    city = ['Singapore','Delhi','Chicago','Almaty']
    return city

@pytest.fixture()
def file_write():
    pytest.filename = "file1.txt"
    f = open(pytest.filename, 'w')
    print("File Written with Data.")
    f.write("Pytest is good.")
    f.close()
    f = open(pytest.filename, 'r+')
    yield f
    print("\n File Available for reading")
    f.close()
    os.remove(pytest.filename)
    print("\n File is deleted after, test execution.")
