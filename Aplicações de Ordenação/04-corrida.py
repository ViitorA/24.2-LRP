nCarros,nVoltas = map(int,input().split())

tempoTotal = []

for i in range(nCarros):
    tempoTotal.append(sum(map(int,input().split())))

posicaoFinal = sorted(tempoTotal)

for i in range(3):
    print(tempoTotal.index(posicaoFinal[i])+1)
