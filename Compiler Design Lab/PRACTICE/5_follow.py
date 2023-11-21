grammar = [
    ["A", "abBdB"],
    ["A", "def"],
    ["B", "@"]
]

#Getting Non Terminals
non_terminals = []
for i in range(0, len(grammar)):
    if grammar[i][0] not in non_terminals:
        non_terminals.append(grammar[i][0])

#Getting Terminals
terminals = []
for i in range(0, len(grammar)):
    for j in range(0, len(grammar[i][1])):
        if grammar[i][1][j] not in non_terminals:
            terminals.append(grammar[i][1][j])

first = {}
for i in range(0, len(non_terminals)):
    first.update({non_terminals[i]: []})

def findFirst(nonTerm, grammar, terminals, first):
    for i in range(0, len(grammar)):
        if(grammar[i][0] == nonTerm):
            if(grammar[i][1][0] in terminals):
                if grammar[i][1][0] not in first[grammar[i][0]]:
                    first[nonTerm].append(grammar[i][1][0])
            else:
                findFirst(grammar[i][1][0], grammar, terminals, first)
                first[nonTerm].extend(first[grammar[i][1][0]])

for i in range(0, len(non_terminals)):
    findFirst(non_terminals[i], grammar, terminals, first)

follow = {}
for i in range(0, len(non_terminals)):
    follow.update({non_terminals[i]: []})
follow["A"].extend("$")

def findFollow(nonTerm, grammar, terminals, non_terminals, first, follow):
    for i in range(0, len(grammar)):
        for j in range(0, len(grammar[i][1])):
            if nonTerm == grammar[i][1][j]:
                if j + 1 == len(grammar[i][1]):
                    findFollow(grammar[i][0], grammar, terminals, non_terminals, first, follow)
                    follow[nonTerm].extend(follow[grammar[i][0]])
                else:
                    if grammar[i][1][j + 1] in terminals and grammar [i][1][j + 1] not in follow[nonTerm]:
                        follow[nonTerm].extend(grammar[i][1][j + 1])
                    elif grammar[i][1][j + 1] in non_terminals and grammar [i][1][j + 1] not in follow[nonTerm]:
                        follow[nonTerm].extend(first[grammar[i][1][j + 1]])

for i in range(0, len(non_terminals)):
    findFollow(non_terminals[i], grammar, terminals, non_terminals, first, follow)

print(first, follow)