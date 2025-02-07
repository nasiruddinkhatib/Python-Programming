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
