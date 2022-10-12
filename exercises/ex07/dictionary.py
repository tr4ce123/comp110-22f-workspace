"""EX 07 - Practicing dictionary functions."""

__author__ = "730567386"


def invert(initial_dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and the values in a given dictionary."""
    inverted_dict: dict[str, str] = {}

    for key in initial_dictionary: 
        if initial_dictionary[key] in inverted_dict:
            raise KeyError("Dictionary has duplicate keys!")
        inverted_dict[initial_dictionary[key]] = key
    return inverted_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """Returns the color in the dictionary that appears the most."""
    color_freq: dict[str, int] = {}
    most_freq_color: str = ""
    maximum_number: int = 0

    for name in color_dict:
        if color_dict[name] not in color_freq:
            color_freq[color_dict[name]] = 1
        else: 
            color_freq[color_dict[name]] += 1

    for colors in color_freq:
        if maximum_number < color_freq[colors]:
            maximum_number = color_freq[colors]
            most_freq_color = colors

    return most_freq_color


def count(str_list: list[str]) -> dict[str, int]:
    """Returns a dictionary where the keys are each unique value in the list and the values are how many times each appears in the list."""
    result: dict[str, int] = {}
    
    for item in str_list: 
        if item not in result:
            result[item] = 1
        else: 
            result[item] += 1 

    return result