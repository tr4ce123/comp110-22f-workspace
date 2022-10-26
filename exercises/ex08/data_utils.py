"""Dictionary related utility functions."""

__author__ = "730567386"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)
    
    # Close that file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table: 
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row: 
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first N rows of data for each column."""
    for col in table:
        if rows > len(col):
            return table 

    result: dict[str, list[str]] = {}
    
    for col in table:
        n_values: list[int] = []
        col_item: list[int] = table[col]
        i: int = 0
        while i < rows:
            n_values.append(col_item[i])
            i += 1 
            
        result[col] = n_values

    return result


def select(table: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    """Produces a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for item in col_names:
        result[item] = table[item]

    # values: list[int] = []
    # col_item: list[int] = table[col]
    # keys: list[str] = []

    # i: int = 0

    # for col in table: 
    #     keys.append(col)

    # while i < len(col_names):
    #     if col_names[i] == keys[i]:
    #         result[keys[i]] = table[keys[i]]
    #     i += 1

    # for col in table: 
    #     i: int = 0
    #     while i < len(col_names):
    #         if col_names[i] == col:
    #             result[col] = table[col]
    #             values.append(col_item[i])
    #             result[col] = values
    #         i += 1

    return result


def concat(initial_table: dict[str, list[str]], add_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}

    for col in initial_table:
        result[col] = initial_table[col]

    for col in add_table:
        if col in result:
            result[col] += add_table[col]
        else: 
            result[col] = add_table[col]
    
    return result