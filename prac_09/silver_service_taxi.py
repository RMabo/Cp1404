"""
CP1404/CP5632 Practical
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness."""

    flagfall = 4.50  # class variable

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness  # fanciness attribute
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like a Taxi but with flagfall added."""
        return f"{super().__str__()}, plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.flagfall + super().get_fare()