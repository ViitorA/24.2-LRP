I,N = map(int,input().split())

#                    D,E,F
dinheiroJogadores = [I,I,I]

for n in range(N):
    entrada = list(input().split())

    if entrada[0] == 'C':
        entrada[2] = int(entrada[2])
        if entrada[1] == 'D':
            dinheiroJogadores[0] -= entrada[2]
        elif entrada[1] == 'E':
            dinheiroJogadores[1] -= entrada[2]
        else:
            dinheiroJogadores[2] -= entrada[2]
    elif entrada[0] == 'V':
        entrada[2] = int(entrada[2])
        if entrada[1] == 'D':
            dinheiroJogadores[0] += entrada[2]
        elif entrada[1] == 'E':
            dinheiroJogadores[1] += entrada[2]
        else:
            dinheiroJogadores[2] += entrada[2]
    elif entrada[0] == 'A':
        entrada[3] = int(entrada[3])
        if entrada[1] == 'D' and entrada[2] == 'E':
            dinheiroJogadores[0] += entrada[3]
            dinheiroJogadores[1] -= entrada[3]
        elif entrada[1] == 'D' and entrada[2] == 'F':
            dinheiroJogadores[0] += entrada[3]
            dinheiroJogadores[2] -= entrada[3]
        elif entrada[1] == 'E' and entrada[2] == 'D':
            dinheiroJogadores[1] += entrada[3]
            dinheiroJogadores[0] -= entrada[3]
        elif entrada[1] == 'E' and entrada[2] == 'F':
            dinheiroJogadores[1] += entrada[3]
            dinheiroJogadores[2] -= entrada[3]
        elif entrada[1] == 'F' and entrada[2] == 'D':
            dinheiroJogadores[2] += entrada[3]
            dinheiroJogadores[0] -= entrada[3]
        elif entrada[1] == 'F' and entrada[2] == 'E':
            dinheiroJogadores[2] += entrada[3]
            dinheiroJogadores[1] -= entrada[3]

print(dinheiroJogadores[0],dinheiroJogadores[1],dinheiroJogadores[2])