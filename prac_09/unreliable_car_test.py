"""
CP1404/CP5632 Practical
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    """Test for UnreliableCar class."""
    my_car = UnreliableCar("Car", 100, 50) # 50% reliability
    good_car = UnreliableCar("Good Car", 100, 90) # 90% reliability
    bad_car = UnreliableCar("Bad Car", 100, 9) # 9% reliability

    for i in range(1, 12): # drive 1-11km each time (inclusive) to test drive() method
        print(f"Attempting to drive {i}km:")
        print(f"{my_car.name} drove {my_car.drive(i)}km") # drive() returns distance driven
        print(f"{good_car.name} drove {good_car.drive(i)}km")
        print(f"{bad_car.name} drove {bad_car.drive(i)}km")

    print(my_car) # print the final states of each car
    print(good_car)
    print(bad_car)


main()
