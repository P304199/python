from string import ascii_lowercase
sentence = input("Enter a sentence: ")
list = []
for i in sentence: 
    if i.lower() in "abcdefghijklmnopqrstuvwxyz":
        if i.lower() not in list:
            list.append(i.lower())
if len(list) == 26:
    print("The sentence is a panagram")
else:
    print("The sentence is not a panagram")