#1] Write a program in python that takes two lists and returns True if they have at least one common member.
def chk_list(list_1, list_2):  
    for item in list_1:  # Iterate through each element in list_1
        if item in list_2:  # Check if the element exists in list_2
            return True  # Return True immediately if a common element is found
    return False  # Return False if no common elements are found after the loop

list_1 = [1, 2, 3, 4, 5]  # Define the first list
list_2 = [7, 8, 9, 9, 2]  # Define the second list
result = chk_list(list_1, list_2)  # Call the function and store the result
print(result)  # Print True if common elements exist, otherwise False
#*******-----**********------*********-----*********----*********----******-----*****----****--**---**--**-*-*-*
#2] Write a program To Written the Compare two list and return the common elements from the list?
l1 = [1, 2, 3, 4, 6, 4]  # List 1 with some duplicate elements
l2 = [9, 8, 7, 2, 4, 6]  # List 2 with unique elements
common_list = list(set(l1) & set(l2))  #Convert lists to sets, find common elements using '&', and convert back to a list

print(common_list)  # Print the list of common elements
#Output:[2, 4, 6]
