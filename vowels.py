#python program to program to count no. if vowels in the string
string =input("enter the string :")
vowels = "a,e,i,o,u,A,E,I,O,U"    #include both uppercase and lowercase vowels
count = 0
for char in string:
    if char in vowels:   # To check if the character is vowel
        count +=1    # increment the count

print(f"The number of the vowels in the string is :{count}")

