# Define the operator precedence table
operators = ["+", "-", "*", "/", "(", ")", "i", "$"]
prec = [
    [">", ">", "<", "<", "<", ">", ">", ""],
    [">", ">", "<", "<", "<", ">", ">", ""],
    [">", ">", ">", ">", "<", ">", ">", ""],
    [">", ">", ">", ">", "<", ">", ">", ""],
    ["<", "<", "<", "<", "<", "=", ">", ""],
    [">", ">", ">", ">", "=", ">", ">", ""],
    ["<", "<", "<", "<", "<", "<", "=", ""],
    ["", "", "", "", "", "", "", ""],
]


# Helper function to get the index of an operator
def getindex(c):
    if c in operators:
        return operators.index(c)
    return -1


# Operator precedence parsing algorithm
def operator_precedence_parser(input_str):
    input_str += "$"
    stack = ["$"]
    i = 0
    valid = True

    while i < len(input_str) and valid:
        top = stack[-1]
        if top == "$" and input_str[i] == "$":
            break
        prec_val = prec[getindex(top)][getindex(input_str[i])]

        if prec_val == "<" or prec_val == "=":
            stack.append(input_str[i])
            i += 1
        elif prec_val == ">":
            popped = stack.pop()
            while not (prec[getindex(stack[-1])][getindex(popped)] == "<"):
                popped = stack.pop()
        else:
            valid = False

    return valid


# Main function to check the validity of a string
def main():
    input_str = input("Enter the string: ")
    is_valid = operator_precedence_parser(input_str)

    if is_valid:
        print("String is valid.")
    else:
        print("String is not valid.")


if __name__ == "__main__":
    main()
