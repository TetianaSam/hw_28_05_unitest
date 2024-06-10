from calculator import Calculator
from view_input import Console

def menu_controller(strategy):
    a = Console.input_number()
    b = Console.input_number()
    c = Console.input_number()

    try:
        result = strategy(a,b,c)
        Console.print_result(result)
    except ValueError as e:
        Console.message_wrong_input(e)

def run():
    k = Calculator()

    choice = -1
    while choice != 0:
        Console.print_menu()
        choice = Console.input_choice(4)

        if choice == 1:
            menu_controller(k.add)

        elif choice == 2:
            menu_controller(k.multiply)

        else:
            Console.message_wrong_input()

run()

