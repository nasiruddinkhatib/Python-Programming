# Program to check palindrome

s = input("enter the value : ")
reverse = s[::-1]
if s == reverse :
    print("Yes It is a palindrome number")
else:
    print("Not a palindrome")