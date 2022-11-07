"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt 


__author__ = "730567386"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
        """Caclulates the distance between two points."""
        result: float = sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
        return result 


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Tick."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()

    def contract_disease(self) -> None:
        """Assigns the infected constant to the sickness attribute."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Returns True when the sickness attribute is vulnerable and False if it is not."""
        if self.sickness == constants.VULNERABLE: 
            return True
        else: 
            return False

    def is_infected(self) -> bool:
        """Returns True when the sickness attribute is infected and False if it is not."""
        if self.sickness >= constants.INFECTED:
            return True
        else: 
            return False

    def color(self) -> str:
        """Assigns the cell the color gray if vulnerable, and another color if not."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_infected():
            return "hot pink"
        elif self.is_immune():
            return "cornflower blue"

    def contact_with(self, other: Cell) -> None:
        """Infects the vulnerable cell if either are infected."""
        if self.is_vulnerable() and other.is_infected():
            self.contract_disease()
        elif self.is_infected() and other.is_vulnerable():
            other.contract_disease()

    def immunize(self) -> None:
        """Assigns immune constant to the cell's sickness attribute."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Returns True when the sickness attribute is immune and False if it is not."""
        if self.sickness == constants.IMMUNE:
            return True
        else: 
            return False


class Model:
    """The state of the simulation."""
    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int, immune = 0):
        """Initialize the cells with random locations and directions."""
        if infected >= cells or infected <= 0:
            raise ValueError("Must have less infected cells than total cells or more than 0 infected cells.")

        if immune >= cells or immune < 0:
            raise ValueError("Must have less immune cells than total cells.")

        self.population = []
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)

        i: int = 0
        while i < infected:
            self.population[i].contract_disease()
            i += 1

        i = 0
        while i < immune:
            self.population[i].immunize()
            i += 1
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        elif cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        elif cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        elif cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        """Scans all cells and changes their color to become infected if they come in contact with an infected cell."""
        counter: int = 0
        while counter < len(self.population):
            i = counter + 1
            while i < len(self.population):
                cell_1: Cell = self.population[counter]
                cell_2: Cell = self.population[i]
                if cell_1.location.distance(cell_2.location) < constants.CELL_RADIUS:
                    cell_1.contact_with(cell_2)
                i += 1
            counter += 1

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        alt_list: list[Cell] = []
        complete: bool = False
        for item in self.population:
            if item.is_vulnerable() or item.is_immune():
                alt_list.append(item)
                if len(alt_list) == len(self.population):
                    complete = True
        
        if complete:
            return True
            