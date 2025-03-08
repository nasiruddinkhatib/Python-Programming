# **************************************** Copy Operation *****************************
# Three Types of Copy Operations:
# 1. General Copy
# 2. Shallow Copy
# 3. Deep Copy

# ********************** General Copy **************************
l = [1, 2, 3, 4]  # Original list
k = l              # General copy: both variables point to the same list

print(l)          # Output: [1, 2, 3, 4]
print(id(l))      # Memory address of l
print(id(k))      # Memory address of k (same as l)

# Disadvantage of General Copy:
# Any change made to one list will reflect in the other since they share the same memory location.

# ********************** Shallow Copy **************************
l = [1, 2, 3, 4]      # Original list
m = l.copy()          # Shallow copy: creates a new list, but only one level deep

l[1] = 10            # Modifying the original list
print(m)             # Output: [1, 2, 3, 4] - remains unchanged
print(l)             # Output: [1, 10, 3, 4] - reflects the change

# Disadvantage of Shallow Copy:
# Shallow copy only copies the outer object, not nested objects.
# If the list contains mutable objects like other lists, changes to those objects
# will reflect in both the original and the copied list.

# Example of the disadvantage:
nested_list = [[1, 2], [3, 4]]
shallow_copy = nested_list.copy()
nested_list[0][0] = 99

print(nested_list)    # Output: [[99, 2], [3, 4]]
print(shallow_copy)   # Output: [[99, 2], [3, 4]] - also reflects the change

# ********************** Deep Copy **************************
import copy

nested_list_deep = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(nested_list_deep)

nested_list_deep[0][0] = 42

print(nested_list_deep)  # Output: [[42, 2], [3, 4]]
print(deep_copy)         # Output: [[1, 2], [3, 4]] - remains unchanged

# Advantage of Deep Copy:
# Deep copy creates a completely independent copy of the original object,
# including all nested objects. Changes to the original object do not affect the copy.
