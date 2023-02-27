"""Ex04_utils."""
__author__ = "730400592"


def all(ints: list[int], integer: int) -> bool:
    """return a bool indicating whether or not all the ints in the list are same as the given int"""
    index: int = 0
    correctness: int = 0
    while index < len(ints):
        if ints[index] == integer:
            correctness += 1
        index += 1
    if correctness == len(ints):
        return True
    else:
        return False


def max(ints: list[int]) -> int:
    """Max will return the largest in the list"""
    if len(ints) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        index: int = 0
        current_max = ints[index]
        while index < len(ints):
            if ints[index]>current_max:
                current_max = ints[index]
            index += 1
        return current_max


def is_equal(ints: list[int], ints2: list[int]) -> bool:
    """Given two lists of int values, return True if every element at every index is equal in both lists"""
    if ints == ints2:
        return True
    else:
        return False