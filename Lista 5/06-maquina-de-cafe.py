n = []

# 1a -> 2a (*2)
# 1a -> 3a (*4)
# 2a -> 1a (*2)
# 2a -> 3a (*2)
# 3a -> 2a (*2)
# 3a -> 1a (*4)

for i in range(0,3):
    n.append(int(input()))

tempo = []

for i in range(0,3):
    if i == 1:
        tempo.append(n[i]*2)
        tempo.append(n[i]*2)
    else:
        tempo.append(n[i]*2)
        tempo.append(n[i]*4)

indexMaiorValor = tempo.index(max(tempo))
tempo.pop(indexMaiorValor)
tempo.pop(indexMaiorValor-1)

tempoGasto = 0

if indexMaiorValor < 2: # [1,1,..]
    tempoGasto = tempo[0]+tempo[3]
elif indexMaiorValor < 5: # [0,0,1,1,...]
    tempoGasto = tempo[0]+tempo[2]
else: # [....,1,1]
    tempoGasto = tempo[1]+tempo[2]

print(tempoGasto)


