#1
password ="code123"
print(len(password))

if len(password) < 8:
    print("password is too short")
else:
    print(password)


#2
num = 5

if num%5 == 0 or num%3 == 0:
    print("This number is divisible by 3 or 5")
else:
    print("This number is not dividible by 3 or 5")

#3
num = 21

if num%7 == 0 and num%3 == 0:
    print("Fizz Buzz")
elif num%3 == 0:
    print("Fizz")
elif num%7 == 0:
    print("Buzz")
else:
    print(num)

#4
word = "Softwares"

print(word[0])
print(word[-1])

if word.lower()[0] == word.lower()[-1]:
    print("True")
else:
    print("False") 

#5
time = 18
place_of_work = "Code Nation"
town_of_home = "Chester"

if time < 8:
    print(f"I'm at home in {town_of_home} having breakfast")
elif time == 8:
    print(f"I am on way to {place_of_work}")
elif time >= 9 and time <= 17:
    print(f"I am at {place_of_work} ")
elif time == 18:
    print(f"I am going back to home in {town_of_home}")
else:
    print(f"I am at home in {town_of_home}")

#6
num1 = 3
num2 = 5

if (num1 + num2)%2 == 0:
    print(f"The sum of {num1} and {num2} is even")
else:
    print("The sum of the 2 numbers is odd")

#7
num = 1001
reversedNum = str(num)[::-1]

if str(num) == reversedNum:
    print("Yes the number is a palindrome")
else:
    print("Number is not a palindrome")

#8
string = "rfndkIhgfndjkjlkgperfijfhdknsadcjhiiohjfkledsopiuhgt yujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi"
last_index = -1

if string.lower().rfind("a") > last_index:
    last_index = string.lower().rfind("a")
if string.lower().rfind("e") > last_index:
    last_index = string.lower().rfind("e")
if string.lower().rfind("i") > last_index:
    last_index = string.lower().rfind("i")
if string.lower().rfind("o") > last_index:
    last_index = string.lower().rfind("o")
if string.lower().rfind("u") > last_index:
    last_index = string.lower().rfind("u")

print(f"The index of the last vowel is {last_index}")











