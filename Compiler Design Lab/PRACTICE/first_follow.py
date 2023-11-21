def first_sets(grammar, non_terminals, terminals):
    first_sets = {}

    for NT in non_terminals:
        first_sets[NT] = set()
    for NT in non_terminals:
        first_sets_rec(grammar, non_terminals, terminals, first_sets, set(), NT)
    return first_sets


def first_sets_rec(grammar, non_terminals, terminals, first_sets, visited, symbol):
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
                    first_sets_rec(
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


if __name__ == "__main__":
    grammar = {
        "E": ["TK"],
        "K": ["+TK", "ε"],
        "T": ["FL"],
        "L": ["*FL", "ε"],
        "F": ["i", "(E)"],
    }
    terminals = {"+", "*", "(", ")", "i"}
    non_terminals = {"E", "K", "T", "L", "F"}
    epsilon = "ε"

    first_sets = first_sets(grammar, non_terminals, terminals)

    print("FIRST sets:")
    for symbol, first_set in first_sets.items():
        print(f"FIRST({symbol}): {first_set}")
