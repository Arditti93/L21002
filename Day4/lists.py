#Starter Activity
# number_1 = int(input("Please enter number 1 "))
# number_2 = int(input("Please enter number 2 "))

# def multiply (num1, num2):
#     print(num1 * num2)

# multiply(number_1,number_2)


# def multiply2 (num1, num2):
#     return num1 * num2


# print(multiply2(2,3))


coffee_order = [
    "Alex - Flat White",
    "james - Latte",
    "Alice - Hot Chocolate"
]

# printing the whole list 
print(coffee_order)

# accessing indavidual items in our list and printing it
# Python is indexed from zero so we start counting from 0 in a list
print(coffee_order[1])

coffee_order[1] = "Emily - Black Coffee"
print(coffee_order)

# counts the items in the list, doesn't count from zero
print(len(coffee_order))
 
# adds an item to the end of the list
coffee_order.append("Ben - Whatever is new")

print(coffee_order)

#removes item from the end of the list
coffee_order.pop()

print(coffee_order)


