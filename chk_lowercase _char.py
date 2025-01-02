#No.of lower case characters from the string.
a= "NasI"
count = 0
for i in a:
    if i.islower():
        count +=1

print("LowerCase Characters:" , count)