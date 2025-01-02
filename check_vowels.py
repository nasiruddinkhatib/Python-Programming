#1]Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise
# def chk_vowel(char):
#     vowels = "aeiouAEIOU"
#     return char in vowels
# print(chk_vowel('a'))  # True
# print(chk_vowel('b'))  # False
# print(chk_vowel('A'))  # True
# print(chk_vowel('E'))  # True

#2]Same Code
# a = "aeiou"
# n=  "xyz"
# if any (vowel in n for vowel in a):
#     print("it a vowel ")
# else:
#     print("Entered Words are not a Vowels")

#3] Same Code
vowels = "aeiouAEIOU"
a = input("Enter the Words you want: ")
if any(char in vowels for char in a ) :
    print("this contains vowels ")
else:
    print("Sorry ! Its Not Contain any Vowels in it ")
