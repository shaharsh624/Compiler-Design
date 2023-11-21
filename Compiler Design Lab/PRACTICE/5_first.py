def calculate_first(grammar, non_terminals, terminals):
    first_sets = {}

    for NT in non_terminals:
        first_sets[NT] = set()
    for NT in non_terminals:
        calculate_first_rec(grammar, non_terminals, terminals, first_sets, set(), NT)
    return first_sets


def calculate_first_rec(grammar, non_terminals, terminals, first_sets, visited, symbol):
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
                    calculate_first_rec(
                        grammar,
                        non_terminals,
                        terminals,
                        first_sets,
                        visited,
                        sub_symbol,
                    )
                    first_sets[symbol].update(first_sets[sub_symbol])
                    if epsilon not in first_sets[sub_symbol]:
                        break

    return


# GRAMMAR-1
# grammar = {
#     "E": ["TK"],
#     "K": ["+TK", "ε"],
#     "T": ["FL"],
#     "L": ["*FL", "ε"],
#     "F": ["i", "(E)"],
# }
# terminals = {"+", "*", "(", ")", "i"}
# non_terminals = {"E", "K", "T", "L", "F"}
# epsilon = "ε"

# GRAMMAR-2
# grammar = {
#     "E": ["E+T", "E-T", "T"],
#     "T": ["T*F", "T/F", "F"],
#     "F": ["X^F", "X"],
#     "X": ["-P", "P"],
#     "P": ["(E)", "i"],
# }
# terminals = {"+", "-", "*", "/", "^", "(", ")", "i"}
# non_terminals = {"E", "T", "F", "X", "P"}
# epsilon = "ε"

# GRAMMAR-3
grammar = {"E": ["T", "a"], "T": ["E", "b"]}

terminals = {"a", "b"}
non_terminals = {"E", "T"}
epsilon = "ε"

calculate_first_set = calculate_first(grammar, non_terminals, terminals)
print("FIRST sets:")
for symbol, first_set in calculate_first_set.items():
    print(f"FIRST({symbol}): {first_set}")
