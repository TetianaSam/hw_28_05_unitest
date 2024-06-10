from converter import Converter
from view_input import Console

def menu_controller(strategy):
    meters = Console.input_metrics()


    try:
        result = strategy(meters)
        Console.print_result(result)
    except ValueError as e:
        Console.message_wrong_input(e)

def run():
    conv = Converter()

    choice = -1
    while choice != 0:
        Console.print_menu()
        choice = Console.input_choice(4)

        if choice == 1:
            menu_controller(conv.meters_to_miles())

        elif choice == 2:
            menu_controller(conv.meters_to_yards())

        elif choice == 3:
            menu_controller(conv.meters_to_inches())

        else:
            Console.message_wrong_input()

run()

