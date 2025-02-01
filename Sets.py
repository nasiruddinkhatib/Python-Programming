#*-*-*-*-*-*-*-SETS IN PYTHON*-*-*-*-*-*-*-*-*-*-*
# A set is a built-in data type in Python used to store unordered, unique elements.
# It is useful for operations that require uniqueness, like removing duplicates or mathematical set operations.
# Properties of Sets
# Unordered → The elements do not have a fixed order.
# Unique Elements → Duplicate values are automatically removed.
# Mutable → You can add or remove elements after creation.
# Heterogeneous → Can contain different data types.
# Unindexed → You cannot access elements using an index.
#**-**-****-***Basics Operations On sets*****-*-*-***--*
S1={'nasir',1,2.1,True}  # It is Unordered means every time you run the different Outputs You get
S2={1,2,3,4,4,5}
print(S1,S2)            # Print sets
print(len(S1))       # calculate Length of Set
s3=set()       #This way we can create a empty set
print(s3)
print(len(S2))  # Length checking to S2
print(S1.pop())  # Remove Item and Give name of the removed elements


#*-*-*-*-*-*-*-***Sets Operations*-*-*-*-*-*-*-*-**
set1 = {1, 2, 3, 4, 5}
print(set1)  # Output: {1, 2, 3, 4, 5}

set2 = set([1, 2, 2, 3, 4, 4, 5])
print(set2)  # Output: {1, 2, 3, 4, 5} (duplicates removed)

empty_set = set()  # Correct way In this way you can print a empty sets
wrong_set = {}     # This creates an empty dictionary, not a set
print(type(empty_set))  # Output: <class 'set'>
print(type(wrong_set))  # Output: <class 'dict'>

#Sets Method Add,Update,Remove
#set = {1,2,4,5,5}
#set.add(10) # Add method of sets but we can add only one element to add more use update method
# set.update([22,23,25,30])  # Update Method we can add more elements.
# set.remove(4)              # remove method
#set.clear()               # Clear the entire set data
# print(set)

#Quetions When to Use Sets?
# 1]Removing Duplicates from a List
# numbers = [1, 2, 2, 3, 4, 4, 5]  # This is a list
# un = set(numbers)  # Convert list to a set (removes duplicates)
# print(un)  # Output: {1, 2, 3, 4, 5}

# 2]Checking Membership Quickly
# vowels = {"a", "e", "i", "o", "u"}
# print("e" in vowels)  # Output: True
#3] Finding Common Elements
# students_a = {"Alice", "Bob", "Charlie"}
# students_b = {"Bob", "David"}
# print(students_a & students_b)  # Output: {'Bob'}
