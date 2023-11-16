"""
CP1404/CP5632 Practical
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test code for SilverServiceTaxi class."""
    my_silver_taxi = SilverServiceTaxi("Silver Taxi", 100, 2)
    my_silver_taxi.drive(18)
    print(my_silver_taxi)
    print(my_silver_taxi.get_fare())


main()
