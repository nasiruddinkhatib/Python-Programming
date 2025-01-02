# ) Write a python program to copy a list

# l1 = [1,"nasir",3,4]
# l2=l1
# print(l2)

#Write a python program to create a list and display all elements less than 5.
# l1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# print("elements less than 5:")
# for i in l1:
#     if i<5:
#         print(i)

# Write a Python program to print a specified list after removing the 0th, 2nd, 4th and 5th elements.
original_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Create a new list excluding the specified indices
# Use a list comprehension to filter out elements at indices 0, 2, 4, and 5
filtered_list = [original_list[i]
                 for i in range(len(original_list))
                 if i not in [0, 2, 4, 5]]
# Print the new list
print("Original list:", original_list)
print("List after removing 0th, 2nd, 4th, and 5th elements:", filtered_list)
