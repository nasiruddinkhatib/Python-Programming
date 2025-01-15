#program to add two numbers using function by taking parameters
# def add (a,b):
#     return a+b
#
# result = add(10,20)
# print(result)
#
# def subract(a,b):
#     return a - b
# result = subract(20,10)
# print(result)

# program To convert celsius to Fahrenheit with using return statement

# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32   # formula to convert Celsius to Fahrenheit
#     return fahrenheit
#
# temp_f= celsius_to_fahrenheit(25)
#
# print(temp_f)

#program to convert Celsius to Fahrenheit without using return statement

# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     print(fahrenheit)
#
# celsius_to_fahrenheit(50)


# program to convert Celsius to Fahrenheit by taking user input
# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32   # formula to convert Celsius to Fahrenheit
#     return fahrenheit
#
# temp_c = float(input("Enter temperature in Celsius: "))
# temp_f = celsius_to_fahrenheit(temp_c)

# print(f"{temp_c}°C is equal to {temp_f}°F") # we used f string to print the result

# 3] Use function and write a program to print table of any number
#
# def print_table(number):  # this is the function and number is the parameter
#     for i in range(1, 11):    # range function is used to print the table from 1 to 10
#         print(f"{number} x {i} = {number * i}") # logic to print the table example 5 x 1 = 5
#
# a = int(input("Enter a number: "))  # we used int function to take user input
# print_table(a)                       # we used print_table function

# 4] Write a program to print the factorial of the number 5
# def factorial(n):  # this is the function and n is the parameter
#     if n == 0:     # if n is 0 then the factorial is 1
#         return 1
#     else:
#         return n * factorial(n - 1)  # logic to print the factorial example 5! = 5 * 4 * 3 * 2 * 1
# num = int(input("Enter a number: "))  # we used int function to take user input
# print(f"The factorial of {num} is {factorial(num)}")  # we used f string to print the result

# factorial program without using function and  by not taking user input
# num = 5
# factorial = 1  # 1 is the initial value
# for i in range(1,num+1):#  range function is used to print the numbers between 1 to 5
#     factorial *= i          # *= is used to multiply the numbers
# print(f"The factorial of the number {num} is {factorial}")     # f is used to print the string