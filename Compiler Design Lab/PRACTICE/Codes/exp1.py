import tokenize
import io
import keyword

# Function to classify and print tokens
def classify_token(tok_type, tok_string):
    if tok_type == tokenize.NAME:
        if tok_string in keyword.kwlist:
            print(f"Keyword: {tok_string}")
        else:
            print(f"Identifier: {tok_string}")
    else:
        print(f"Other: {tok_string}")

# Open the input file
file_path = "PRACTICE\Codes\python.txt"  # Change this to the path of your input file
with open(file_path, 'rb') as file:
    tokens = tokenize.tokenize(file.readline)

    for tok in tokens:
        classify_token(tok.type, tok.string)

# Close the file
file.close()
