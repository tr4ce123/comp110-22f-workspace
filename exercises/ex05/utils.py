"""EX 05 - Building list utility functions."""

__author__ = "730567386"

def only_evens(number_list: list[int]) -> list[int]:
    """Returns only the even values from a given list of ints as a new list."""
    
    i: int = 0
    even_list: list[int] = list()

    while i < len(number_list):
        if number_list[i] % 2 == 0:
            even_list.append(number_list[i])
        
        i += 1
    
    return even_list


def concat(number_list1: list[int], number_list2: list[int]) -> list[int]:
    """Generates a new list that contains all elements of the first list followed by all elements of the second list."""

    i: int = 0
    combined_list: list[int] = list()

    while i < len(number_list1):
        combined_list.append(number_list1[i])
        i += 1

    i: int = 0

    while i < len(number_list2):
        combined_list.append(number_list2[i])
        i += 1
    
    return combined_list

def sub(number_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Generates a list that is a subset of the given list between the starting and ending indices."""

    sub_list: list[int] = list()
    length_of_list = len(number_list)

    if start_index < 0:
        start_index = 0

    if end_index > len(number_list): 
        end_index = -1

    if len(number_list) == 0 or start_index > len(number_list) or start_index == len(number_list):
        return sub_list

    if end_index < 0:
        end_index = length_of_list

    while end_index > start_index:
        sub_list.append(number_list[start_index])

        start_index += 1
    
    return sub_list