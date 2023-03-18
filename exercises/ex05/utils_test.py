"""Utils_test."""
__author__ = "730400592"

from exercises.ex05.utils import only_evens, sub, concat


def test_with_even() -> None:   # use case
    """Test the list that contains even number."""
    assert only_evens([1, 2, 3]) == [2]


def test_without_even() -> None:   # use case
    """Test the list that doesn't contain even number."""
    assert only_evens([1, 5, 3]) == []


def test_empty() -> None:    # edge case
    """Test empty list."""
    assert only_evens([]) == []


def test_lists_with_same_length() -> None:   # use case
    """Test two lists with same length."""
    list_1: list[int] = [1, 2, 3]
    list_2: list[int] = [4, 5, 6]
    assert concat(list_1, list_2) == [1, 2, 3, 4, 5, 6]


def test_lists_with_different_lenth() -> None:    # use case
    """Test two lists with different length."""
    list_1: list[int] = [1, -2, 3]
    list_2: list[int] = [4, -5]
    assert concat(list_1, list_2) == [1, -2, 3, 4, -5]


def test_two_empty_lists() -> None:   # edge case
    """Test two empty lists."""
    list_1: list[int] = []
    list_2: list[int] = []
    assert concat(list_1, list_2) == []


def test_return_many_elements() -> None:   # use case
    """Test when difference between start and end index is more than 1."""
    list_1: list[int] = [1, 2, 3, 4]
    assert sub(list_1, 1, 4) == [2, 3, 4]


def test_return_one_element() -> None:    # use case
    """Test when difference between start and end index is 1."""
    list_1: list[int] = [1, 2, 3, 4]
    assert sub(list_1, 1, 2) == [2]


def test_empty_list() -> None:   # edge case
    """Test the empty list."""
    list_1: list[int] = []
    assert sub(list_1, 1, 3) == []