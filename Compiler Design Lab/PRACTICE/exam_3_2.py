grammar = {
    "E": ["E+T", "T"],
    "T": ["T*F", "F"],
    "F": ["id"],
}


terminals = {"a", "b"}
non_terminals = {"E", "T"}
for symbol in non_terminals:
    for production in grammar[symbol]:
        if production[0] == symbol:
            print(f"Left recursion in {production}")
            