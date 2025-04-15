# print fibonacci series
def fib(n):
    a = 0
    b = 1

    if n == 1:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)
# Call the function 
fib(10)  # You can replace 10 with any positive integer ypu want 

#*******-*-*-*-*-*-***-Same Code Using User Input*-*-*-*-*-*-*-*-***----*****---***--***---****---****---***--
# using user input
a = 0
b = 1
num = int(input("enter the number to obtain Fibonacci series: "))
if num == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2, num):
        c = a+b
        a=b
        b=c
        print(c)

#****************-------------**************----------*****************
# Fibonacci series using recursion 
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
for i in range(5):
    print(fibonacci(i), end=" ")
#Output:
#0 1 1 2 3 



# Fibonacci series using Recursion by taking user input 
def fibbon(n):
    if n==0:
         return 0
    elif n==1:
          return 1
    else:
          return fibbon(n-1)+fibbon(n-2)
num=int(input("Enter The Number :"))       
for i in range(0,num):
    print(fibbon(i),end=' ')

# Output :
# Enter The Number :
# 6
# 0 1 1 2 3 5 
        
            
