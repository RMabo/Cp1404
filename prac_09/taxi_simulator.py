"""
CP1404/CP5632 Practical

Write a taxi simulator program that uses your Taxi and SilverServiceTaxi classes.

Each time, until they quit:

The user should be able to choose from a list of available taxis,
They can choose how far they want to drive,
At the end of each trip, show them the trip cost and add it to their bill.
Use a list of taxi objects, which you create in main and pass to functions that need it.
When you choose the taxi object, your code will call the drive() method on that object, and it will use the right method for that class... so from the client code point of view, driving a taxi will work the same whether the object is a Taxi or a SilverServiceTaxi, but the results (including the price) depend on the class.
This is polymorphism.

In this program, there's the chance the user will
drive a taxi before choosing one. This shouldn't crash.
A good option is to maintain something like a current_taxi... but what will the initial value of this variable be?
When you want a default starting value for an object, don't use a string or other unrelated type...
Instead, you use None:

current_taxi = None
The taxis used in the example below would be like:

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU: str = """q)uit, c)hoose taxi, d)rive"""


def main():
    """Taxi simulator program that uses your Taxi and SilverServiceTaxi classes."""
    print("Let's drive!")
    total_cost = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None # current taxi is equal to none
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
            print("Bill to date: ${:.2f}".format(total_cost))
        elif menu_choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                distance_to_drive = float(input("Drive how far? "))
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_cost))
                total_cost += trip_cost
                print("Bill to date: ${:.2f}".format(total_cost))
        else:
            print("Invalid option")
        print(MENU)
        menu_choice = input(">>> ").lower()
    print("Total trip cost: ${:.2f}".format(total_cost))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis): # function to display the taxis
    """Display taxis."""
    for i, taxi in enumerate(taxis): # for each taxi in the list of taxis in the main function
        print(f"{i} - {taxi}") # prints the index and the taxi details from the list of taxis in the main function


main()
