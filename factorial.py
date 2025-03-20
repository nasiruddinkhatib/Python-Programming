#***********---------************----- Factorial Program**********------**********-------************
# In short, a factorial is a function that multiplies a number by every number below it till 1.
# For example, the factorial of 3 represents the multiplication of numbers 3, 2, 1, i.e. 3! = 3 × 2 × 1 and is equal to 6.
def fac(n):
    if n==0:  # Factorial of 0 is 1
        return 1
    return n*fac(n-1)     
result=fac(3)
print(result)

#**********Same factorial program Using User Input************--------*********
def fac(n):
    if n==0:  # Factorial of 0 is 1
        return 1
    return n*fac(n-1)
num=int(input("Enter the number: "))
result=fac(num)
print(result)
