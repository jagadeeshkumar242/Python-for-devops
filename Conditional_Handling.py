# import sys
# type = sys.argv[1]

type = input("Kindly enter your instance type: ")
if type == "t2.micro":
    print("Ok, this will charge 2$ per hour")
elif type == "t2.medium":
    print("OK, this will charge 3$ per hour")
elif type == "x3.large":
    print("OK, this will charge 5$ per hour")
else:
    print("Sorry, please provide the correct instance")
