# Program to print a Armstrong number
num = int(input("Enter the number here: "))      # Prompt the user to enter a number

# Initialize variables
sum = 0        # To store the sum of the cubes of the digits
temp = num     # Temporary variable to process the number without altering the original

# Loop through each digit of the number
while temp > 0:
    digit = temp % 10         # Extract the last digit of the number
    cube = digit ** 3         # Calculate the cube of the digit
    sum = sum + cube          # Add the cube to the sum
    temp //= 10               # Remove the last digit from the number

# Check if the sum of the cubes is equal to the original number
if sum == num:
    print("It is an Armstrong number")  # Output if the number is an Armstrong number
else:
    print("Not an Armstrong number")    # Output if the number is not an Armstrong number
