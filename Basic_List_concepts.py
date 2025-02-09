# What is List in python ?
# A list in Python is a collection of items that are ordered, changeable (mutable), and allow duplicate values.
# Lists are one of the most commonly used data types in Python because they are versatile and easy to use.
#The first item has an index of 0, the second has an index of 1, and so on.
#********----------***********----------------**********--------************---------********----*********-*-*-*-*-
numbers = [10,0,-1,7,10,85] # list name if numbers here you can take any name as your choice 
#mix_list=["school",1,"college",2,"Graduate",8.1,"complete"] # So List can contain multiple data type in it
#print(len(numbers))   # len is use to calculate tha length of data present in it
#print(max(numbers))   # Give the largest number present in numbers list
#print(min(numbers))   # Give tha Smallest number
#print(numbers.sort()) # It will give You None so don't code in this type
#numbers.sort()        # Code like this to sort numbers
#print(numbers)
#numbers.reverse()     # Code for reverse list you also use -1 either to reverse
#print(numbers)
#numbers.append(50)    # this function will add 50 at end in numbers only 1 number we can add using append
#print(numbers)
# if you want to add numbers at specific index then mention index number****----****-----**--
#numbers.insert(1,30) # Insert functions is used to add numbers at any index append only add data at end
#print(numbers)
# If You want to add more than 1 numbers use extend keyword method*****-----****---
numbers = [10,0,-1,7,10,85]  
numbers.extend([22,23,100]) # Here We Added more  numbers in the list 
print(numbers)
#print(numbers[0:5])   # Print from index 0 till 5  Output : 10,0,-1,7,10
#print(numbers[1:5])   # print from index 1 till 5  Output : 0,-1,7,10
#print(numbers[0:5:2]) # it will jump 2 step Output : 10, -1, 10
#print(numbers[:])     # it will print all the data of the list
#print(numbers[-1])    # Print from backward
#print((numbers[1:4])  # Index will start from 1 to 3
#if You want to add more number use extend function but it will only add at End side
# numbers.extend([40,50,90,100])
# print(numbers)
# numbers.remove(0)  # It will remove the number
# print(numbers)
# numbers.pop()    # Pop Will remove the number of the end
# print(numbers)
# numbers.clear()   # clear All The list
# print(numbers)
#*******List Concatenation*******
l1 =["Nasir","Maths","Science",True,1,2]    #list 1
l2 =[1,2,3]                                 #list 2
print(l1+l2)                                 #adding l1 to t2 Concatenation
print(l2*2)   #To repeat the elements of the list * is use so the element will get two time Output:[1, 2, 3, 1, 2, 3]

#*******LOOPS in list*******
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:                    # FOR LOOP
    print(fruit)

fruits = ["apple", "banana", "cherry"]
i = 0                                    # WHILE LOOP
while i < len(fruits):
    print(fruits[i])
    i += 1

