from pytest_bdd import scenario, scenarios, given, when, then
from pathlib import Path
import pytest


featureFileDir = 'feature_dir'
featureFile = 'test_1.feature'

BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

def pytest_configure():
    pytest.AMT = 0

scenarios(FEATURE_FILE)

# @scenario(FEATURE_FILE, 'Withdrawal of Money')
# def test_withdrawal():
#     print(f"Test: Withdrawal of Money - Completed")
#     pass


@given('The account balance is 100')
def starting_balance():
    pytest.AMT = 100
    print(f"\nStarting account balance {pytest.AMT}")


@when('The account holder withdraws 30')
def withdrawal_request():
    pytest.AMT -= 30
    print("\nAmount deducted = 30")


@then('The account balance remaining should be 70')
def check_balance():
    print(f"\nRemaining Amount = {pytest.AMT}")
    assert pytest.AMT == 70

# @scenario(FEATURE_FILE,"Removal of items from set")
# def test_itemRemovalFromSet():
#     print("Test: Removal of Item from Test - Completed")
#     pass

@given("A set of 3 fruits",target_fixture="fruits")
def setOfFruits():
    fruits = {"apple", "mango", "banana"}
    print(f"\nFruits in set: {fruits}")
    return fruits

# To use the paramater fruits, we need to define special parameter called `target_fixture`.

@when("We remove a fruit from the set")
def removeFruits(fruits):
    print(f"\nFruit removed: {fruits.pop()}")
    print(f"\nRemaining Fruits: {fruits}")

@then("The set will have 2 fruits")
def remainderFruits(fruits):
    try:
        assert len(fruits) == 2
        print("\nThere are now 2 fruits in set.")
    except Exception as e:
        print(f"\nUnknown error occurred: {e}")
