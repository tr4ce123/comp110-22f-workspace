"""Test for utils functions."""

__author__ = "730567386"

from exercises.ex05.utils import only_evens, concat, sub


def test_only_evens_odds_only() -> None:
    """Should give back an empty list when all values in given list are odd."""
    number_list: list[int] = [1, 3, 5, 7]
    assert only_evens(number_list) == list()


def test_only_evens_both_odd_and_even() -> None:
    """Has both even and odd values but should only return the even values as a new list."""
    number_list: list[int] = [1, 2, 6, 8, 5, 9, 10]
    assert only_evens(number_list) == [2, 6, 8, 10]


def test_only_evens_empty() -> None:
    """Should return a new empty list if the given list is empty."""
    number_list: list[int] = []
    assert only_evens(number_list) == list()


def test_concat_both_empty() -> None:
    """Should give back a new empty list if both given lists are empty."""
    number_list1: list[int] = []
    number_list2: list[int] = []
    assert concat(number_list1, number_list2) == list()


def test_concat_one_empty() -> None:
    """Should give back the values of the list that isn't empty as a new list."""
    number_list1: list[int] = []
    number_list2: list[int] = [1, 3, 5, 6, 8, 9]
    assert concat(number_list1, number_list2) == [1, 3, 5, 6, 8, 9]


def test_concat_both_full() -> None:
    """Should output a new list that contains the values of the first list followed by the values of the second list in order."""
    number_list1: list[int] = [1, 2, 3, 4]
    number_list2: list[int] = [5, 6, 7, 8]
    assert concat(number_list1, number_list2) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_sub_list_empty() -> None:
    """Should automatically give back a new empty list because the given list is empty."""
    number_list: list[int] = []
    start_index: int = 0
    end_index: int = 3
    assert sub(number_list, start_index, end_index) == list()


def test_sub_end_index_negative() -> None:
    """Should make the end index equal to the last index when it is less than zero, making the list go from the start index all the way to the end of the list."""
    number_list: list[int] = [1, 2, 3, 4]
    start_index: int = 0
    end_index: int = -4
    assert sub(number_list, start_index, end_index) == [1, 2, 3, 4]


def test_sub_both_positive() -> None: 
    """Should give back a new list containing the values of the given list starting at the start index and ending at the end index(non inclusive)."""
    number_list: list[int] = [1, 2, 3, 4]
    start_index: int = 0
    end_index: int = 3
    assert sub(number_list, start_index, end_index) == [1, 2, 3]