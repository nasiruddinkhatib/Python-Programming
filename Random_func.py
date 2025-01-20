# Basic Program to Import a random function and print head ant tail possibilities  if 0 head and for tail 1
# import random
# s=random.randint(0,1)
# print(s)
# if s==1:
#     print("Its is a head ")
# if s==0:
#     print(" Its a Tail")

# Same Program different method
# import random
# n = int(input("enter the possibly"))
# side=random.randint(0,1)
# if side==0 or side==0:
#     print("head")
# elif side==1 or side==1:
#     print("Tail")

# Write a program select a random name from a list of names and the person selected will have to pay everybody's bill
# Importing the random module to use random functions
import random
# Taking a comma-separated string of names as input
name = input("Enter the names separated by commas: ")
# Splitting the input string into a list of names
name_list = name.split(",")
# Randomly selecting a name from the list and printing who will pay
print(f"{random.choice(name_list)} will pay the bill")
