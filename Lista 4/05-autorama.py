nPostos,nCarros,nLeituras = map(int,input().split())

leituras = []
posicao = [0]*nCarros

for m in range(nLeituras):
    leituras.append(list(map(int,input().split())))

for i in range(nLeituras):


print(leituras)
print(posicao)
