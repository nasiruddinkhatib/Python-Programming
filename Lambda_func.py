# what is Lambda Function in Python ?
# Python Lambda Functions are anonymous functions means that the function is without a name.
# As we already know the def keyword is used to define a normal function in Python.
# Similarly, the lambda keyword is used to define an anonymous function in Python.
#1] Program
s1 = 'GeeksforGeeks'
s2 = lambda func: func.upper()
print(s2(s1))

# 2] Program Using lambda
sq = lambda x: x ** 2
print(sq(3))

# Using function
# def sqdef(x):
#     return x ** 2
# print(sqdef(3)
#
# 3] Program
# # Using for loop conditions
# li = [lambda arg=x: arg * 10 for x in range(1, 5)]    # arg will iterate from index 1 to 4 (1,5) 1,2,3,4
# for i in li:
#     print(i())
#Output:10 20 30 40

# 4] Program Even Odd Checking using Lamda
# a=int(input("Enter the Number:"))
# check = lambda x:"Even " if x%2==0 else "Odd "
# print(check(a))

# 5]Find Avg USing Lambda
avg = lambda x,y,z: x+y/z
print(avg(10,20,70))
