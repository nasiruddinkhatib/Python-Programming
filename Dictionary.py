# What is Dictionary?
# A Python dictionary is a data structure that stores the value in key: value pairs {}.
# Values in a dictionary can be of any data type and can be duplicated, whereas keys can’t be repeated and must be immutable.
# Key-Value Pair Structure: Each element in a dictionary has a key and an associated value.
# A dictionary in Python is a built-in data structure that stores data in key-value pairs.
# It is an unordered, mutable, and indexed collection that allows you to efficiently retrieve, update, or manipulate data using keys.
# Keys must be unique and immutable (like strings, numbers, or tuples), while values can be of any data type and can be duplicated.

#Example Key Apple - Value = 50,   apple price is 50 key is apple value is 50

d1 ={"Apple":50,"Banana":40,"Kiwi":100}
print(type(d1))    # Type of data
print(d1.keys())   # Keys of d1
print(d1.values()) # Values of d1
print(d1["Apple"])  # Access a Specific Value Retrieve the value for a specific key:

d1["mango"]=100     # Add a New Key-Value Pair Add an item to the dictionary:
print(d1)

d1["apple"]=120  # Update the Value of a Key Update an existing item:
print(d1)

del d1["Banana"]  # Delete an Item Remove an item using its key:
print(d1)

# value = d1.pop("Kiwi")  # Using pop() Remove an item and retrieve its value:
# print("Removed value:", value)
# print(d1)

# for key in d1.keys(): #Loop Through Keys Iterate through all the keys:
#     print(key)

# for value in d1.values():  #  Loop Through Values Iterate through all the values:
#     print(value)

# for key, value in d1.items(): #  Loop Through Key-Value Pairs Use items() to iterate over both keys and values:
#     print(f"{key}: {value}")

#*******Update Method********
dictionary = {"name": "Nasir"}        # Creating the First dictionary
dic2 = {"age": 25, "city": "Mumbai"}  # Creating the second dictionary
dictionary.update(dic2)               # Using the update() method to merge dic2 into dictionary
print("Updated Dictionary:", dictionary) #Printing the updated dictionary

#Output: Updated Dictionary: {'name': 'Nasir', 'age': 25, 'city': 'Mumbai'}


