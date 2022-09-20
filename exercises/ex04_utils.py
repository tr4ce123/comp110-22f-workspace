"""EX 04 - Implementing algorithms to practice computational thinking."""

__author__ = "730567386"


def all(number_list: list[int], number: int) -> bool:
    """Scans the list to show that the single number is equal to every value in the list."""
    i: int = 0

    if len(number_list) == 0: 
        return False

    while i < len(number_list): 
        if number != number_list[i]:
            return False 

        i += 1

    return True 


def max(input: list[int]) -> int:
    """Scans list of integers and returns the largest value."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    i: int = 1
    maximum_value: int = input[0]

    while i < len(input):
        if maximum_value < input[i]:
            maximum_value = input[i]
            
        i += 1
    
    return maximum_value


def is_equal(int_list1: list[int], int_list2: list[int]) -> bool:
    """Compares the indices of each list to show whether they have the same contents or not."""
    i: int = 0
    if len(int_list1) != len(int_list2): 
        return False 

    while i < len(int_list1): 
        if int_list1[i] != int_list2[i]: 
            return False
        i += 1

    return True 