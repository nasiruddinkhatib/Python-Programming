#Enter the number from the user and depending on whether the number is even or odd, print out an appropriate message to the user.
def check_even_odd():
    # Ask the user to enter a number
    number = int(input("Enter a number: "))

    # Check if the number is even or odd
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")

check_even_odd()
