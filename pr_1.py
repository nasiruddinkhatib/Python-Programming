# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
import datetime

# Ask the user for their name
name = input("Enter your name: ")

# Ask the user for their age
age = int(input("Enter your age: "))

# Get the current year
current_year = datetime.datetime.now().year

# Calculate the year the user will turn 100
year_turn_100 = current_year + (100 - age)

# Print a message to the user
print(f"{name}, you will turn 100 years old in the year {year_turn_100}.")
