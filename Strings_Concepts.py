### Basic String Operations
# Creating strings
simple_string = "Hello, Python!"
multiline_string = '''This is
a multiline
string.'''

# Accessing characters
print(simple_string[0])     # H
print(simple_string[-1])    # !

# Slicing
print(simple_string[0:5])   # Hello
print(simple_string[:5])    # Hello
print(simple_string[7:])    # Python!

# String length
print(len(simple_string))   # 13

# String methods
print(simple_string.lower())        # hello, python!
print(simple_string.upper())        # HELLO, PYTHON!
print(simple_string.replace("Python", "World"))  # Hello, World!
print(simple_string.split(","))    # ['Hello', ' Python!']

# Checking substrings
print("Python" in simple_string)    # True

### String Formatting
name = "Nasiruddin"
age = 22

# Using f-strings
print(f"My name is {name} and I am {age} years old.")

# Using format method
print("My name is {} and I am {} years old.".format(name, age))

### Advanced String Techniques
# Joining and Splitting
words = ["Python", "is", "awesome"]
print(" ".join(words))             # Python is awesome

# Stripping whitespace
messy_string = "   Hello, World!   "
print(messy_string.strip())         # Hello, World!

# Advanced slicing and reversing
print(simple_string[::-1])          # !nohtyP ,olleH

#*********Regular Expressions Python************
#We’re importing Python’s built-in re (regular expressions) module. This gives us powerful tools for matching and searching patterns in
#strings.
### Regular Expressions Code:
import re
text = "The rain in Spain"
match = re.search("rain", text) #re.search("rain", text) looks for the first occurrence of the word "rain" in the string.
if match:
    print("Match found!")

# Finding all words starting with 'S'
print(re.findall(r'\bS\w+', text)) # ['Spain']
#Output :
# Match found!
# ['Spain']


#******************************String Practice Questions*********************
##1)Python Program to Replace all Occurrences of ‗d‘ with $ in a String
# Define the input string
a = "Nasiruddin"  # The original string where replacements will be made
b = a.replace("d", "$")  # The replace() method is used to replace 'd' with '$' in the string
print(b)
# Output : Nasiru$$in

##2))  replace blank space in a string.
a="Nasir and Nasir"
b=a.replace(" ","-")
print(b)
#Output :
#Nasir-and-Nasir
