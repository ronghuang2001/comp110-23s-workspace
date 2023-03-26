"""Ex07 Dictionary."""
__author__ = "730400592"


def invert(dictionary: dict[str,str]) -> dict[str,str]:
    """Return a dictionary that inverts keys and values of input dictionary."""
    dictionary_1: dict[str,str] = dict() 
    list_1: list[str] = list()
    index: int = 0
    playing: bool = True
    playing_2: bool = True
    duplicate: bool = False
    for item in dictionary:
        list_1.append(dictionary[item])
    while index < len(list_1) and playing is True:
        index_check = 0
        while index_check < len(list_1) and playing_2 is True:
            if list_1[index_check] == list_1[index] and index_check != index:
                playing_2 = False
                playing = False
                duplicate = True
            else:
                index_check += 1
        index += 1
    if duplicate is True:
        raise KeyError
    else:
        for item in dictionary:
            dictionary_1[dictionary[item]] = item
        return dictionary_1
    

def favorite_color(dictionary: dict[str, str]) -> str:
    list_1: list[str] = list()
    max_occurrence: int = 0
    index: int = 0
    index_check: int = 0
    color_appear_most: str = ""
    for item in dictionary:
        list_1.append(dictionary[item])
    while index < len(list_1):
        index_check = 0
        current_occurrence: int = 0
        while index_check < len(list_1):
            if list_1[index_check] == list_1[index]:
                current_occurrence += 1
            index_check += 1
        if current_occurrence > max_occurrence:
            max_occurrence = current_occurrence
            color_appear_most = list_1[index]
        index += 1
    return color_appear_most


def count(list_1: list[str]) -> dict[str,int]:
    dictionary_1: dict[str,int] = dict()
    for item in list_1:
        if item in dictionary_1:
            dictionary_1[item] += 1
        else:
            dictionary_1[item] = 1
    return dictionary_1




    