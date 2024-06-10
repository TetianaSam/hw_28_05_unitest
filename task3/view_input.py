class Console:
    @staticmethod
    def print_menu():
        print("""
        -------MENU----
        [1] Convert meters to miles 
        [2] Convert meters to inches
        [3] Convert meters to yards
        [0] The end 
        """)

    @staticmethod
    def message_wrong_input(message="Wrong input"):
        print(message)

    @staticmethod
    def input_choice(num):
        choice = -1
        while not choice in range(num+1):
            choice = input("Chose your variant: ")

            try:
                choice = int(choice)
            except ValueError:
                Console.message_wrong_input()
                choice = -1

        return choice

    @staticmethod
    def input_metrics():
        num = ""
        while type(num) != type(0):
            num = input("zadej mnozstvi metru: ")

            try:
                num = int(num)
            except ValueError:
                Console.message_wrong_input()
                num = ""

        return num

    @staticmethod
    def print_result(result):
        print(f"Your result is: {result}")
