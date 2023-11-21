import re


def identify(word):
    if word in keywords:
        return "Keyword"
    elif word in seperators:
        return "Seperator"
    elif word in operators:
        return "Operator"
    elif word in specials:
        return "Special"
    return "Identifier"


if __name__ == "__main__":
    keywords = [
        "print",
        "False",
        "None",
        "True",
        "and",
        "as",
        "assert",
        "break",
        "class",
        "continue",
        "def",
        "del",
        "elif",
        "else",
        "except",
        "finally",
        "for",
        "from",
        "global",
        "if",
        "import",
        "in",
        "is",
        "lambda",
        "nonlocal",
        "not",
        "or",
        "pass",
        "raise",
        "return",
        "try",
        "while",
        "with",
        "yield",
    ]
    seperators = [",", ";"]
    specials = ["!", "@", "#", "$", "&", "?"]
    operators = ["%", "^", "*", "(", ")", "-", "+", "="]

    with open("1_input.py", "r") as f:
        words = f.read().split()

        for j in words:
            print(f"{identify(j)}: {j}")
