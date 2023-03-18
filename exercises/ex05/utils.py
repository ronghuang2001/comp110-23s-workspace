"""EX05_utils."""
__author__ = "730400592"


def only_evens(int_list: list[int]) -> list[int]:
    """Return a new list containing only even elements in the input list."""
    integer_list: list[int] = list()
    for item in int_list:
        if item % 2 == 0:
            integer_list.append(item)
    return integer_list


def concat(int_list1: list[int], int_list2: list[int]) -> list[int]:
    """Return a new list which contains all elements of the first list followed by all elements of the second list."""
    integer_list: list[int] = list()
    for item in int_list1:
        integer_list.append(item)
    for item in int_list2:
        integer_list.append(item)
    return integer_list


def sub(int_list: list[int], index1: int, index2: int) -> list[int]:
    """Return a list which is a subset of the given list, between the specified start index and the end index - 1."""
    integer_list: list[int] = list()
    if len(int_list) == 0 or index1 >= len(int_list) or index2 <= 0:
        return integer_list
    if index1 < 0:
        index1 = 0
    if index2 > len(int_list):
        index2 = len(int_list)
    for idx in range(index1, index2):
        integer_list.append(int_list[idx])
    return integer_list