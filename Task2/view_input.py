class Console:
    @staticmethod
    def print_menu():
        print("""
        -------MENU----
        [1] The max of 3 numbers
        [2] The min of 3 numbers
        [3] The mean of 3 numbers
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
    def input_number():
        num = ""
        while type(num) != type(0):
            num = input("zadej čislo: ")

            try:
                num = int(num)
            except ValueError:
                Console.message_wrong_input()
                num = ""

        return num

    @staticmethod
    def print_result(result):
        print(f"Your result is: {result}")


