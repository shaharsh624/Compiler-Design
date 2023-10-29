# A program to read letter file and identify keywords, identifiers and others
import keyword
import string

keywords = []
identifier = []
others = []

alphabet = list(string.ascii_lowercase)

with open('python.txt', 'r') as f:
    letter = f.read().split()
print(letter)
for i in range(len(letter)):
    if letter[i] in keyword.kwlist:
        if letter[i] not in keywords:
            keywords.append(letter[i])
            print(letter[i], "is keyword")
    elif letter[i] in alphabet:
        if letter[i] not in identifier:
            identifier.append(letter[i])
            print(letter[i], "is identifier")
    else:
        if letter[i] not in others:
            others.append(letter[i])
            print(letter[i], "is others")

print(keywords)
print(identifier)
print(others)