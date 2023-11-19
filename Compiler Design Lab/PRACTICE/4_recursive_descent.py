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
    if string[lookahead] == 'i':
        print('E')
        print('E->', end="")
        match('i')
        F()

def F():
    if string[lookahead] == "+":
        print('F')
        print('F->', end="")
        match("+")
        match("i")
        F()


def match(char):
    global lookahead
    global string

    if (string[lookahead] == char):
        print(char, end="")
        lookahead += 1
    else :
        raise ValueError("ERROR")


if __name__ == "__main__":
    E()
    if (string[lookahead] == "$"):
        print("\nThe String has been parsed successfully!")
    else:
        print("\nThe String couldn't be parsed!")