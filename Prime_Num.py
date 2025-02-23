#***************************************Prime Number ***********************************************
##Programme to Check The given number is Prime Or Not 
num=int(input("Enter a number:"))
for i in range(2,num):
    if num % i ==0:
       print("It's a Prime number ")
       break

else:
    print("OOPS! It's Not a Prime Number ")
# Output :
# Enter a number: 7
# It's a Prime number
