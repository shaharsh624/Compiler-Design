'''
E –> E + T | T 
T –> T * F | F 
F –> ( E ) | id
'''
# Because the grammar has left recursion, it can't be parsed by recursive Descent Parser

global lookahead
global string
lookahead = 0
string = input("Enter string to parse: ")

def E():
    E()
    if (string[lookahead] == '+'):
        print('E')
        print('E', end='->')
        match('+')
        T()
    else:
        T()
        
def T():
    T()
    if (string[lookahead] == '*'):
        print('T')
        print('T', end='->')
        match('*')
        F()
    else :
        F()

def F():
    if (string[lookahead] == '('):
        print('F')
        print('F', end='->')
        match('(')
        E()
        match(')')
    elif (string[lookahead] == 'i'):
        match('i')
    else:
        return

def match(c):
    global lookahead
    global string
    if (string[lookahead] == c):
        print(c, end='->')
        lookahead += 1
    else:
        print("ERROR")

if __name__ == "__main__":
    E()
    if (string[lookahead] == '$'):
        print("\nThe string has been parsed successfully")
    else:
        print("\nThe string could not be parsed")
