age = int(input("What is ur Age? "))
if 18 <= age <= 65:
    print("Have a good day at work")
else:
    print("Enjoy ur free time")
print("~" * 70)
if age < 18 or age > 65:
    print("Enjoy the free time")
else:
    print("Have a great day for ur work")
# ###########################################################################
activity = input("What would you like to do today?")
if "cinema" not in activity.casefold():  # not in example
    print("But I want to go to Cinema")
else:
    print("Lets go for Cinema")
##########################################################################
name = input("Enter ur name")
for char in name:
    if not char.islower():  # if char is uppercase
        print(char)
age = int(input("Enter Ur age"))
if 18 < age < 31:
    print("You are welcome to the Holiday")
else:
    print("Sorry U r not supposed to come for Holiday")
##############################################################################
for i in range(0, 11, 2):  # step by 2 from 0 to 11
    print(f"i is now {i}")
for i in range(10, 0, -2):  # step by -2 from 10 to 1
    print(f"i is now {i}")
