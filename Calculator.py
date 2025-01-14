# Function to add Two Numbers
def add(num1, num2):
    return num1 + num2

# Function to Subtract Numbers
def subtract(num1, num2):
    return num1 - num2

# Function to Multiply Numbers
def multiply(num1, num2):
    return num1 * num2

# Function to Divide Numbers
def divide(num1, num2):
    return num1 / num2

# Function to Average Two Numbers
def avg(num1, num2):
    return (num1 + num2) / 2

# Step 2: Take User Input
print("Please Select an Operation:\n"
      "1. Addition\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Division\n"
      "5. Average\n")

# Take user input
select = int(input("Select the Operation from 1, 2, 3, 4, 5: "))
number1 = int(input("Enter the First Number: "))
number2 = int(input("Enter the Second Number: "))

# Step 3: Print the Result
if select == 1:
    print(number1, "+", number2, "=", add(number1, number2))
elif select == 2:
    print(number1, "-", number2, "=", subtract(number1, number2))
elif select == 3:
    print(number1, "*", number2, "=", multiply(number1, number2))
elif select == 4:
    print(number1, "/", number2, "=", divide(number1, number2))
elif select == 5:
    print("Average of", number1, "and", number2, "=", avg(number1, number2))
else:
    print("Invalid Operation. Please select again.") # Print an error message if 1,2,3,4,5 is not selected



