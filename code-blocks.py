for i in range(1, 11):
    print("No. {} squared is {} cubes is {:4}".format(i, 1 ** 2, i ** 3))
print("*" * 80)
########################################################################
#  If block
###############
name = input("Enter Ur name")
age = int(input("Enter your age"))

if age < 18:
    print("Cannot Vote")
elif age == 18:
    print("U r eligible")
else:
    print("Can vote")
