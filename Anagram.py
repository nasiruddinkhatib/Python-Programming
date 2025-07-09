#######################################-Anagram In python-#########################################################
#An anagram is a word, phrase, or sequence of characters formed by rearranging the letters of another, 
# using all the original letters exactly once.
# For example:
# "listen" and "silent" are anagrams because they contain the exact same letters arranged differently.
# "banana" and "bnanaa" are also anagrams because they have the same letters, just in a different order.
#Code : 
# Define two strings to compare
a = "banana"  # String 1
b = "bnanaa"  # String 2

# Check if the sorted characters of both strings are equal
if sorted(a) == sorted(b):  
    print("It's an anagram")  # If sorted strings match, they are anagrams
else:
    print("Not an anagram")  # If sorted strings do not match, they are not anagrams
    
#Output : 
#It's an anagram    

'''Both strings "banana" and "bnanaa" contain the exact same characters with the same frequency — just in a 
different order. Sorting them puts their characters in the same sequence: ['a', 'a', 'a', 'b', 'n', 'n'].
Since the sorted versions match, they are considered anagrams.'''
