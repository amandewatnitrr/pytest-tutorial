from pytest_bdd import scenario, scenarios, when, then, given, parsers
from pathlib import Path
import pytest
from pytest_bdd.generation import print_missing_code

featureFileDir = 'feature_dir'
featureFile = 'scenarioOutline.feature'

BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE=BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

scenarios(FEATURE_FILE)

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
