# Function to calculate FIRST sets
def calculate_first(grammar, non_terminals, terminals):
    first_sets = {}

    for NT in non_terminals:
        first_sets[NT] = set()

    for NT in non_terminals:
        calculate_first_rec(grammar, NT, terminals, first_sets, set())
    return first_sets


def calculate_first_rec(grammar, symbol, terminals, first_sets, visited):
    if symbol in terminals:
        first_sets[symbol].add(symbol)
    elif symbol not in visited:
        visited.add(symbol)
        for production in grammar[symbol]:
            for sub_symbol in production:
                if sub_symbol in terminals:
                    first_sets[symbol].add(sub_symbol)
                    break
                elif sub_symbol == epsilon:
                    first_sets[symbol].add(epsilon)
                else:
                    calculate_first_rec(grammar, sub_symbol, terminals, first_sets, visited)
                    first_sets[symbol].update(first_sets[sub_symbol])
                    if epsilon not in first_sets[sub_symbol]:
                        break

    return


# Example grammar
grammar = {
    "E": ["TK"],
    "K": ["+TK", ""],
    "T": ["FL"],
    "L": ["*FL", ""],
    "F": ["i", "(E)"],
}

terminals = {"+", "*", "(", ")", "i"}
non_terminals = {"E", "K", "T", "L", "F"}
epsilon = ""


# Calculate FIRST sets
first_sets = calculate_first(grammar, non_terminals, terminals)
print("FIRST sets:")
for symbol, first_set in first_sets.items():
    print(f"FIRST({symbol}): {first_set}")
