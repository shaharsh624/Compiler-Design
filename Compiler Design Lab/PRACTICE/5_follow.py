import importlib

first = importlib.import_module("5_first")
calculate_first = first.calculate_first

print(first)

# Function to calculate FOLLOW sets
def calculate_follow(grammar, non_terminals, terminals, first_sets):
    follow_sets = {NT: set() for NT in non_terminals}
    follow_sets[grammar[start]].add('$')

    for NT in non_terminals:
        calculate_follow_rec(grammar, NT, terminals, follow_sets, first_sets, set())

    print("\nFOLLOW sets:")
    for symbol, follow_set in follow_sets.items():
        print(f"FOLLOW({symbol}): {follow_set}")

    return follow_sets

def calculate_follow_rec(grammar, symbol, terminals, follow_sets, first_sets, visited):
    if symbol not in visited:
        visited.add(symbol)
        for NT, productions in grammar.items():
            for production in productions:
                for i, sub_symbol in enumerate(production):
                    if sub_symbol == symbol:
                        if i < len(production) - 1:
                            follow_sets[symbol].update(calculate_first_set(production[i + 1:], first_sets, terminals))
                            if epsilon in calculate_first_set(production[i + 1:], first_sets, terminals):
                                follow_sets[symbol].update(calculate_follow_rec(grammar, NT, terminals, follow_sets, first_sets, visited))
                        else:
                            follow_sets[symbol].update(calculate_follow_rec(grammar, NT, terminals, follow_sets, first_sets, visited))
    
    return follow_sets[symbol]

def calculate_first_set(symbols, first_sets, terminals):
    first_set = set()
    for symbol in symbols:
        if symbol in terminals:
            first_set.add(symbol)
            break
        else:
            first_set.update(first_sets[symbol])
            if epsilon not in first_sets[symbol]:
                break
    return first_set

# Example grammar
grammar = {
    "E": ["TK"],
    "K": ["+TK", ""],
    "T": ["FL"],
    "L": ["*FL", ""],
    "F": ["i", "(E)"],
}
start = "E"
terminals = {"+", "*", "(", ")", "i"}
non_terminals = {"E", "K", "T", "L", "F"}
epsilon = ""

# Calculate FIRST sets
first_sets = calculate_first(grammar, non_terminals, terminals)

# Calculate FOLLOW sets
calculate_follow_sets = calculate_follow(grammar, non_terminals, terminals, first_sets)
