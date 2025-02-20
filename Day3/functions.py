# we define our function using the word def, then the name we want to call the function.
# then ():
def press_grind_beans():
    # Code that we wish run inside the function
    # must be indented
    print("grinding beans for 20 seconds")


# Call the function so it runs
# press_grind_beans()


def say_name():
    name = input("Please enter your name: ")
    print(f"Hello {name} welcome to my python code")

say_name()


enter_amount = input("Please enter an amount")
enter_accnum = input ("Please enter an account number")

def cash_machine(amount, accnum):
    print(f"withdrawing {amount} from account number {accnum}")

# cash_machine(400, 565783)
# cash_machine(50, 34687899)
# cash_machine(enter_amount, enter_accnum)



def take_order(size, type_of_drink):
    print(f"I'd like a {size} {type_of_drink} please")

take_order("Small", "Flat White")