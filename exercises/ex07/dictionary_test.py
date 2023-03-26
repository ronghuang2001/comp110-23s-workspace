"""Dictionary Test."""
__author__ = "730400592"


from exercises.ex07.dictionary import invert, favorite_color, count
import pytest
    

def test_without_duplicate() -> None:   # use case
    """Test a dictionary without duplicated values or empty value."""
    assert invert({'a': 'z', 'b' : 'y', 'd': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'd'}


def test_with_duplicate() -> None:   # use case
    """Test a dictionary with duplicated values."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jorda', 'michael': 'jorda'}
        invert(my_dictionary)


def test_with_empty() -> None:   # edge case
    """Test a dictionary with an empty value."""
    assert invert({'a': '', 'b' : 'y'}) == {'': 'a', 'y': 'b'}


def test_without_tie() -> None:    #use case
    "Test a dictionary without tie."
    assert(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"})) == "blue"


def test_with_tie() -> None:    #use case
    "Test a dictionary with tie."
    assert(favorite_color({"Marc": "yellow", "Kris": "blue"})) == "yellow"

def test_with_1_pair() -> None:     #edge case
    "Test a dictionary with only 1 pair."
    assert(favorite_color({"Marc": "yellow"})) == "yellow"


def test_value_occurs_multiple_times() -> None:     #use case
    "Test a list with a value that occurs multiple times."
    assert(count(["a","b","c","a"])) == {'a': 2, 'b': 1, 'c': 1}


def test_value_occurs_1_time() -> None:       #use case
    "Test a list with values that occur only 1 time."
    assert(count(["a","b","c"])) == {'a': 1, 'b': 1, 'c': 1}


def test_empty_list() -> None:       #edge case
    "Test empty list."
    assert(count([])) == {}

