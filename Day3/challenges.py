# Challenge 1 
order_count = 0
# def take_order(topping):
#     global order_count
#     print("Pizza with {}".format(topping))
#     order_count += 1
# take_order("pineapple")

# ---------------------- 
def take_order(topping, topping_2, size):
    global order_count
    print(f"Pizza with {topping}, {topping_2} and size {size}")
    order_count +=1
    print(order_count)

# take_order("Cheese","pepperoni","Small")
# take_order("Anchoives","Tom","Large")

#2
account_balance = 250
account_pin = 1234

def cash_machine(pin, ammount):
    global account_balance

    if pin != account_pin:
        print("Incorrect Pin")
    elif pin == account_pin and ammount <= account_balance:
        account_balance = account_balance - ammount
        print(f"Withdrawing {ammount} new balance is {account_balance}")
    else:
        print("Account balance is too low")


input_pin = int(input("Please enter your pin "))
input_amount = int(input("Please enter an amount "))
cash_machine(input_pin, input_amount)