# A set is a built-in data type in Python used to store unordered, unique elements.
# It is useful for operations that require uniqueness, like removing duplicates or mathematical set operations.
#Properties of Sets
# Unordered → The elements do not have a fixed order.
# Unique Elements → Duplicate values are automatically removed.
# Mutable → You can add or remove elements after creation.
# Heterogeneous → Can contain different data types.
# Unindexed → You cannot access elements using an index.
#**********Sets Operations ********
# set1 = {1, 2, 3, 4, 5}
# print(set1)  # Output: {1, 2, 3, 4, 5}
#
# set2 = set([1, 2, 2, 3, 4, 4, 5])
# print(set2)  # Output: {1, 2, 3, 4, 5} (duplicates removed)

# empty_set = set()  # Correct way In this way you can print a empty sets
# wrong_set = {}     # This creates an empty dictionary, not a set
# print(type(empty_set))  # Output: <class 'set'>
# print(type(wrong_set))  # Output: <class 'dict'>

#Sets Method Add,Update,Remove
#set = {1,2,4,5,5}
#set.add(10) # Add method of sets but we can add only one element to add more use update method
# set.update([22,23,25,30])  # Update Method
# set.remove(4)              # remove method
#set.clear()
print(set)
#Quetions When to Use Sets?
# 1] Removing Duplicates from a List
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}
# 2]Checking Membership Quickly
vowels = {"a", "e", "i", "o", "u"}
print("e" in vowels)  # Output: True
# 3] Finding Common Elements
students_A = {"Alice", "Bob", "Charlie"}
students_B = {"Bob", "David"}
print(students_A & students_B)  # Output: {'Bob'}

