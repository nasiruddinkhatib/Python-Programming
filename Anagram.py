#) To check two strings are anagram or not.

a="banana"  #created s string name as banana
b = "bnanaa"
if sorted(a)==sorted(b):
    print("its a anagram")
else:
    print("Not a anagram")