def reverse_val(value):
    reversed_val = str(value)[::-1]
    return reversed_val

user_value=input("enter a value to reverse:")

result=reverse_val(user_value)
print(f"the reversed value is {result}")

