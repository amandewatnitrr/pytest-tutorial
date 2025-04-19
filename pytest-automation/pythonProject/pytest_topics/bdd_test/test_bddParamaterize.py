from pytest_bdd import scenario, scenarios, when, then, given, parsers
from pathlib import Path
import pytest
from pytest_bdd.generation import print_missing_code

featureFileDir = 'feature_dir'
featureFile = 'test_paramaterzie.feature'

BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE=BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

scenarios(FEATURE_FILE)

@given("There are 3 varieties of fruit",target_fixture="fruits")
def exsistingFruits():
    fruits = {'apple', 'grapes', 'strawberry'}
    print(f"Fruits: {fruits}. There are total of {len(fruits)}")
    return fruits

@when("We add a same variety of fruit")
def addSameFruit(fruits):
    print("\nAdding a fruit that is already there in the set.")
    fruits.add("grapes")

@then("There is same count of varieties")
def same_count(fruits):
    print(f"There are still {len(fruits)} fruit varieties.")
    assert len(fruits) == 3


@then("If we add a different variety of fruit")
def addDiffFruit(fruits):
    print("\nTomato added to fruits")
    fruits.add("Tomato")

@then(parsers.parse("The count of varieties increases to {count:d}"))
def updated_count(fruits,count):
    print(f"\nThere are {count} varieties of fruits.")
    assert len(fruits) == count


# Scenario: Paramaterize Benefits

@given(parsers.parse("We have {count:d} fruits"),target_fixture="start_fruits")
def exsistingFruits(count):
    return dict(start=count,eat = 0)

@when(parsers.parse("I eat {eat:d} fruits"))
def eat3ruits(start_fruits,eat):
    print(f"\nWe have eaten {eat} fruits.")
    start_fruits["eat"] += eat

@then(parsers.parse("I should have {left:d} fruits"))
def shouldHaveFruits(start_fruits,left):
    diff = start_fruits["start"] - start_fruits["eat"]
    print(f"\nWe have {diff} fruits remaining.")
    assert start_fruits["start"] - start_fruits["eat"] == left
