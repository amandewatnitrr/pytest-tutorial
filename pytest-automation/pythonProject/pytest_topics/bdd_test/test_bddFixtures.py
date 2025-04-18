from pytest_bdd import scenario, scenarios, when, then, given
from pathlib import Path
import pytest

featureFileDir = 'feature_dir'
featureFile = 'test_fixture.feature'

BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE=BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

scenarios(FEATURE_FILE)

@pytest.fixture()
def setup_set():
    countries = {"India", "China", "US", "Germany"}
    print(f"Forming Set: {countries}")
    return countries

@given("A datatype set")
def checkSetType(setup_set):
    print("\nChecking Set Type in background...")
    if not isinstance(setup_set,set):
        pytest.xfail("\nDatatype is not set.")
    else:
        print("\nDatatype is set.")

@given("The Set is not empty")
def setNotEmpty(setup_set):
    print("\nChecking set length in background...")
    if(len(setup_set)) <= 0:
        pytest.xfail("\nFailure expected. Set is empty or smaller than expected.")
    elif len(setup_set) == 3 :
        print("\nSet is of desired size.")
    else:
        print("\nSet is bigger than expected. pop() needed.")


@given("Set has 3 elements",target_fixture="setup_set")
def setOfEle(setup_set):
    if len(setup_set) == 0:
        pytest.xfail("Set is empty.")
    elif len(setup_set) > 3:
        while len(setup_set) > 3:
            setup_set.pop()
    return setup_set

@when("We add 2 elements to the set")
def addEleToSet(setup_set):
    setup_set.add("UK")
    setup_set.add("Russia")
    print("\nAdded 2 elements to the set")

@then("Set now has 5 elements")
def checkSet(setup_set):
    print(f"\nSet has {len(setup_set)} elements.")
    assert len(setup_set) == 5
    print("\nSet Length check test completed.")



