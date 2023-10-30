'''
E - iF
F - +iF | !
'''

global lookahead
global string
string = input("Enter the string: ")
string += "$"
lookahead = 0

def E():
    if (string[lookahead] == 'i'):
        print('E')
        print('E', end="->")
        match('i')
        F()

def F():
    if (string[lookahead] == '+'):
        print('F')
        print('F', end="->")
        match('+')
        match('i')
        F()
    else:
        return

def match(c):
    global string
    global lookahead
    if (string[lookahead] == c):
        print(c, end="")
        lookahead += 1
    else:
        print("ERROR")
    
if __name__ == "__main__":
    E()
    if (string[lookahead] == '$'):
        print("\nThe string has been parsed successfully")
    else:
        print("\nThe string could not be parsed")