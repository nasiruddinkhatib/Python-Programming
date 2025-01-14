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
num1 = int(input("Enter the First Num: "))
num2 = int(input("Enter the Second Num: "))

# Step 3: Print the Result
if select == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif select == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))
elif select == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))
elif select == 4:
    print(num1, "/", num2, "=", divide(num1, num2))
elif select == 5:
    print("Average of", num1, "and", num2, "=", avg(num1, num2))
else:
    print("Invalid Operation. Please select again.") # Print an error message if 1,2,3,4,5 is not selected


#OutPut For Code will Like This :
Please Select an Operation:
1. Addition
2. Subtract
3. Multiply
4. Division
5. Average

Select the Operation from 1, 2, 3, 4, 5: 1
Enter the First Num: 10
Enter the Second Num: 20
10 + 20 = 30
