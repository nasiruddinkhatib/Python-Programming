# Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 3, 1]) should print the following:
def histogram(numbers):  #The function histogram() takes a list of integers as input, e.g., [4, 3, 1].
    for num in numbers: #
        print('*' * num)

# Example usage:
histogram([4, 3, 1])
