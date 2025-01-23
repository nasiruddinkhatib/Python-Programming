# What is  Loops ?
# In Python, loops are used to execute a block of code repeatedly. Loops are essential for automating repetitive tasks, iterating through data structures, and much more.
# Python provides two main types of loops: for loops and while loops. 1. For Loop
# The for loop iterates over a sequence (e.g., list, tuple, string, range) and
# executes a block of code for each element.
#Example 1  Iterating through list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
  print(fruit)

#1]write a program to print 1 to 10 using  loop
for i in range(1,11):    #range function is used to print the numbers and 1 is included and 11 is not included so it will print 1 to 10
  print(i,end=" ")        #end=" " is used to print the numbers in a single line

#2]write a program to print the squares of the number from 1 to 5
# for i in range(1,6):
#     print(i ** 2,end=" ")

#3]write a program to print even number between 1 to 10
# for i in range(1,11):  # range function is used to print the numbers between 1 to 10
#   if i % 2 == 0:         # % is used to find the remainder of the number
#    print(i,end=" ")      #end=" " is used to print the numbers in a single line

#4]calculate the sum of the numbers from 1 to 10
# total = 0     #0 is the initial value
# for i in range(1,11):
#     total += i           #+= is used to add the numbers
# print(f"The sum of the Numbers is : {total}")       #f is used to print the string

#5] write a program to print the odd number between 1 to 10
# for i in range(1,11):
#     if i % 2 != 0:  # % is used to find the remainder of the number odd numbers are not divisible by 2
#         print(i,end=" ")

#6] write a program to print the word "python" in reverse order
# word = "python"     # python is the string and word is the variable
# for i in range(len(word)-1,-1,-1):  # len function is used to find the length of the string and -1 is used to print the string in reverse order
#     print(word[i],end=" ")

#7] write a program to count the number of the vowels in the word "python"
# vowels= "aeiou" # a,e,i,o,u are the vowels
# word = "python"      # python is the word we have to count the vowels
# for letter in word:
#     if letter in vowels:
#         print(f"The number of {letter} in the word {word} is {word.count(letter)}") # f is used to print the string and count function is used to count the vowels

 #8] write a program to print fibonacci series upto 10 sequence
# a = 0  # 0 is the initial value
# b = 1  # 1 is the initial value
# print(a,b ,end=" ")    #end=" " is used to print the numbers in a single line
# for _ in range(10):     # _ is used to store temporary variable name  actual value is not important we take 10 beacause we want to print 10 sequence
#     next_term = a + b
#     print(next_term,end=" ")
#     a,b= b,next_term

#9] write a program to print the factorial of the number 5
# num = 5
# factorial = 1  # 1 is the initial value
# for i in range(1,num+1):#  range function is used to print the numbers between 1 to 5
#     factorial *= i          # *= is used to multiply the numbers
# print(f"The factorial of the number {num} is {factorial}")     # f is used to print the string
#
# # 10] write a program to print the prime numbers between 1 to 10
# num = 23   # 23 is the number
# is_prime = True # True is the initial value
# for i in range(2, int(25 **0.5) + 1): #range function is used to print the numbers between 2 to 23
#     if num % i == 0:
#         is_prime = False
#         break
#
# if is_prime and num > 1:
#   print(num, "is a prime number")
# else:
#   print(num, "is not a prime number")

# 11]write a program to count occurrences of each character in a word "programming"
# word = "programming"
#
# for char in word:             #    we are using char variable to store the each character of the word
#     count = word.count(char)    # count function is used to count the characters
#     print(f"The number of {char} in the word {word} is {count}")     # f is used to print the string


# a = "applee"
# for char in a:
#         count = a.count(char)
#
#         print(f"The sum of {char} in the word {a} is {count}")

# 12]write a program to count occurrences of each character in a word "applee" by taking user input
# word = input("Enter the word: ")
#
# for char in word:             # we are using char variable to store the each character of the word
#     count = word.count(char)  # count function is used to count the characters
#     print(f"The number of {char} in the word {word} is {count}")

#**********Loops Using List**********
# l1 = ["Nasir","Amin","Samad","Habib"]
# l2 = ["College", "School","Tuition","University"]
# for i in l1:
#     for j in l2:
#         print(i,j)

#Output:
# Nasir College
# Nasir School
# Nasir Tuition
# Nasir University
# Amin College
# Amin School
# Amin Tuition
# Amin University
# Samad College
# Samad School
# Samad Tuition
# Samad University
# Habib College
# Habib School
# Habib Tuition
# Habib University


