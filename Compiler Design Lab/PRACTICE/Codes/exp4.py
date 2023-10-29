# Grammar

# expr   -> term + expr
#        | term - expr
#        | term

# term   -> factor * term
#        | factor / term
#        | factor

# factor -> ( expr )
#        | num

# num    -> [0-9]+

class RecursiveDescentParser:
    def __init__(self, input_string):
        self.tokens = input_string.replace(" ", "")
        self.current_token = None
        self.token_index = 0

    def get_next_token(self):
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
            self.token_index += 1
        else:
            self.current_token = None

    def expr(self):
        self.term()
        while self.current_token in ('+', '-'):
            op = self.current_token
            self.get_next_token()
            self.term()
            print(op)

    def term(self):
        self.factor()
        while self.current_token in ('*', '/'):
            op = self.current_token
            self.get_next_token()
            self.factor()
            print(op)

    def factor(self):
        if self.current_token == '(':
            self.get_next_token()
            self.expr()
            if self.current_token != ')':
                raise SyntaxError("Expected closing parenthesis")
            self.get_next_token()
        else:
            num = self.num()
            print(num)

    def num(self):
        num = ""
        while self.current_token is not None and self.current_token.isdigit():
            num += self.current_token
            self.get_next_token()
        return num

    def parse(self):
        self.get_next_token()  # Initialize current_token
        self.expr()  # Start parsing from the top-level rule

        # Check for extra tokens
        if self.current_token is not None:
            raise SyntaxError("Unexpected token: " + self.current_token)

# Test the parser
input_string = "2 + 3 * (4 - 1)"
parser = RecursiveDescentParser(input_string)
parser.parse()
