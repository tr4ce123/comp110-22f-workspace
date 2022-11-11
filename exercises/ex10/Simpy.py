"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730567386"


class Simpy:
    """Utility class that is helpful for working with sequences of numerical data."""
    values: list[float]

    def __init__(self, float_list: list[float]):
        """Constructor that initializes values attribute."""
        self.values = float_list

    def __repr__(self) -> str:
        """Is automatically called when a Simpy object is converted to string and overloads it."""
        return f"Simpy({self.values})"

    def fill(self, float_num: float, num_values: int) -> None:
        """Fills a Simpy's values with a specific number of repeating values."""
        self.values = []
        i: int = 0
        while i < num_values: 
            self.values.append(float_num)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values attribute with a range of values."""
        assert step != 0.0

        self.values = []
        self.values.append(start)
    
        while abs(start) < abs(stop - step):
            self.values.append(start + step)
            start += step

    def sum(self) -> float:
        """Computes and returns the sum of all items in the values attribute."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds the ability to use the addition operator in conjunction with Simpy objects and floats."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)

        result: Simpy = Simpy([])

        if isinstance(rhs, float):
            for item in self.values:
                result.values.append(item + rhs)
        else:
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds the ability to use the power operator in conjunction with Simpy objects and floats."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)

        result: Simpy = Simpy([])

        if isinstance(rhs, float):
            for item in self.values:
                result.values.append(item ** rhs)
        else:
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces a mask based on the equality of each item in the values attribute with some other Simpy object or a float value."""
        result: list[bool] = []

        if isinstance(rhs, float):
            for item in self.values:
                if item == rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces a mask based on the greater than relationshiop between each item in the values attribute with some other Simpy object or a float value."""
        result: list[bool] = []

        if isinstance(rhs, float):
            for item in self.values:
                if item > rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Adds the ability to use the subscription operator with Simpy objects."""
        result_float: float = 0.0
        result_Simpy: Simpy = Simpy([])

        if isinstance(rhs, int):
            result_float = self.values[rhs]
            return result_float
        else: 
            for i in range(len(rhs)):
                if rhs[i]:
                    result_Simpy.values.append(self.values[i])
            return result_Simpy
                
        