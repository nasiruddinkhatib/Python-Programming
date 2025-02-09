#1] Write a program in python that takes two lists and returns True if they have at least one common member.
def chk_list(list_1, list_2):
    for item in list_1:
        if item in list_2:
            return True
    return False  # Move this outside the loop

list_1 = [1, 2, 3, 4, 5]
list_2 = [7, 8, 9, 9, 2]
result = chk_list(list_1, list_2)
print(result)  # Output: True

#2] Write a program To Written the Compare two list and return the common elements from the list?
l1 = [1, 2, 3, 4, 6, 4]  List 1 
l2 = [9, 8, 7, 2, 4, 6]  List 2 

common_list=list(set(l1)& set(l2)) #Set method is Use  to remove duplicates because set is use to remove duplicates
print(common_list)
