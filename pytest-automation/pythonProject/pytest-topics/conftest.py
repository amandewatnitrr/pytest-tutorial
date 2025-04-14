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


@pytest.fixture()
def function_detail(request):
    print(f"\nStarting test: {request.node.name}")
    print(f"\nIn Module: {request.module.__name__}")
    print(f"\n Request Scope: {request.scope}")
    print(f"\n Function Name: {request.function.__name__}")
    digits =  getattr(request.module, "digits")
    print(f"\n Digits: {digits}")
    yield
    print(f"\nFinished test: {request.node.name}")

@pytest.fixture()
def return_tuple_or_list():
    def get_dt(name):
        if name == 'list':
            return [1,2,3]
        elif name == 'tuple':
            return (1,2,3)
        else:
            raise ValueError("Invalid type requested")
    return get_dt

@pytest.fixture(params=[(1,2),[3,4]], ids=['tuple', 'list'])
def return_tuple_list(request):
    return request.param