# Write a program in python that takes two lists and returns True if they have at least one common member.
def chk_list(list_1, list_2):
    for item in list_1:
        if item in list_2:
            return True
    return False  # Move this outside the loop

list_1 = [1, 2, 3, 4, 5]
list_2 = [7, 8, 9, 9, 2]
result = chk_list(list_1, list_2)
print(result)  # Output: True


