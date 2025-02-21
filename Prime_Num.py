#*******---------**************Prime Number Or Not*********------------***************-----------********

num=int(input("Enter a number:"))
for i in range(2,num):
    if num % i ==0:
       print("It's a Prime number ")
       break

else:
    print("OOPS! It's Not a Prime Number ")