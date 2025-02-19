music = "classical"

if music == "classical": 
    print("oh no its classical")
elif music == "no music" :
    print("silence")
else:
    print("turn it up")



age = 18
country = "Uk"

if age > 17 and country == "UK":
    print("Yes you can drink and you are in the uk")
else:
    print("No you aren't old enough")

if age >= 18:
    print("Yes you can drink")
else:
    print("No you aren't old enough")


place =  "Manchester"
weather =  "Rain"
# both conditions have to be met with the and operator
if place == "MCR" or place =="Manchester" and weather == "Rain":
    print("Oviously")
elif place == "MCR" or place =="Manchester" and weather == "Sunny":
    print("Check again")
else:
    print("What it isn't raining") 


day = "Monday"
# with or just one of the conditions has to be met
if day == "Saturday" or day == "Sunday":
    print("it's the weekend!")
else:
    print("its not the weekend")