"""
CP1404/CP5632 Practical
"""

from random import randint
from prac_09.car import Car


class UnreliableCar(Car):  # UnreliableCar inherits from Car class
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):  # added reliability parameter to __init__ method and initialised it
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)  # calls the parent class Car's __init__ method
        self.reliability = reliability  # added reliability attribute

    def __str__(self):  # added __str__ method
        """Return a string like a Car but with reliability."""
        return f"{super().__str__()}, reliability={self.reliability}"

    def drive(self, distance):  # added drive method
        """Drive like parent Car but calculate reliability as well."""
        random_number = randint(0, 100)  # generates a random number between 0 and 100
        if random_number < self.reliability:  # if random number is less than reliability
            distance_driven = super().drive(distance)
            return distance_driven
