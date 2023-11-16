"""
CP1404/CP5632 Practical
"""

from prac_09.taxi import Taxi


def main():
    """Test code for Taxi class."""
    my_taxi = Taxi("Prius 1", 100)  # create a new taxi object
    my_taxi.drive(40)  # drive the taxi 40 km
    print(my_taxi)  # print the taxi's details and the current fare
    my_taxi.start_fare()  # restart the meter (start a new fare)
    my_taxi.drive(100)  # drive the car 100 km
    print(my_taxi)  # print the details and the current fare


main()
