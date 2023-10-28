# Recursive Descent Parser

'''
# Grammar:

E - iF
F - +iF | $

# Here '!' is epsilon

'''
print("Grammar used: ")
print("E - iF")
print("F - +iF | $")

global string
string = list(input("Enter the string ending with $: "))
global lookahead
lookahead = 0

def E() :
    if (string[lookahead] == 'i'):
        match('i')
        F()

def F() :
    if (string[lookahead] == '+'):
        match('+')
        match('i')
        F()
    else:
        return
    
def match(c):
    global string
    global lookahead
    if (string[lookahead] == c):
        lookahead += 1
    else:
        print("ERROR")

if __name__ == "__main__":
    E()
    if (string[lookahead] == "$"):
        print("The string is successfully parsed")
    else:
        print("The string could not be parsed")
