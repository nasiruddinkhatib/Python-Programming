# What is tuples ?
# A tuple is a collection which is ordered and unchangeable.
#Tuples are Immutable means (Unchangeable)
# Tuples are written with round brackets().
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary,
# all with different qualities and usage.
# Realtime Uses of tuple  Will Like Storing geographical co-ordinates

t1 = ("nasir",1,True,1.1,100,"Boss")   # tuple 1
#t2 =(2,3,4,50,90,4)                   # tuple 2
#print(type(t1))       # To check type
# print(t1[0])         # It will Print index 0  Output: nasir
# print(t1[1:3])
#print(t1+t2)
# print(max(t2))        # It will print Max Number
# print(min(t2))        # Minimum Number
#************How to Check Tuple Type**************
# n=("nas")
# print(type(n))  # It will Give Output as String not Tuple Beacause for tuple Comma should come if value is single value 
# #Output :  <class 'str'>
a=("nasir",) # We Added Comma(,) to make it tuple because if we dont give comma to this single value it will consider as string 
print(type(a))
#output : <class 'tuple'>

# *****Tuple  Deletion****
# t3 = ("nasir",1,2)
# del t3               # It will Delete tuple Del Keyword is used here simple.


# **********Tuple Deletion*********
# t3 = ("nasir", 1, 2)
# print("Before deletion:", t3)
#
# del t3  # Deletes the tuple
# # Trying to print t3 after deletion will raise an error
# try:
#     print(t3)
# except NameError as e:
#     print("Error:", e)
