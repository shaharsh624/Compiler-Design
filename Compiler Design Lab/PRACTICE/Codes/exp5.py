# Function to calculate FIRST sets
def calculate_first(grammar, non_terminals, terminals):
    first_sets = {}
    for non_terminal in non_terminals:
        first_sets[non_terminal] = set()

    for non_terminal in non_terminals:
        calculate_first_recursive(grammar, non_terminal, first_sets, terminals)

    return first_sets

def calculate_first_recursive(grammar, symbol, first_sets, terminals):
    if symbol in terminals:
        first_sets[symbol].add(symbol)
    else:
        for production in grammar[symbol]:
            prev_symbol = None
            for sub_symbol in production:
                if sub_symbol in terminals:
                    if prev_symbol is not None:
                        calculate_first_recursive(grammar, prev_symbol, first_sets, terminals)
                        if epsilon in first_sets[prev_symbol]:
                            first_sets[symbol] = first_sets[symbol].union(first_sets[prev_symbol])    
                    first_sets[symbol].add(sub_symbol)
                    break
                elif sub_symbol != epsilon:
                    calculate_first_recursive(grammar, sub_symbol, first_sets, terminals)
                    first_sets[symbol] = first_sets[symbol].union(first_sets[sub_symbol])
                    prev_symbol = sub_symbol
                    # if epsilon not in first_sets[sub_symbol]:
                    #     break
                    # elif epsilon in first_sets[sub_symbol]:
                    #     continue
                        
                             
                
# Example grammar
grammar = {
    'S': ['aB', 'bA', 'c'],
    'A': ['Bd', 'e'],
    'B': ['f', 'ε'],
}

start_symbol = 'S'
epsilon = 'ε'
terminals = {'a', 'b', 'c', 'd', 'e', 'f'}
non_terminals = {'S', 'A', 'B'}

# Calculate FIRST sets
first_sets = calculate_first(grammar, non_terminals, terminals)
print("FIRST sets:")
for symbol, first_set in first_sets.items():
    print(f'FIRST({symbol}): {first_set}')