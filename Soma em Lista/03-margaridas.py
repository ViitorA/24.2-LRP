# l -> n linhas
# c -> n colunas
# m -> n linhas lote
# n -> n colunas lote
l,c,m,n = map(int,input().split())

matriz = []

for i in range(l):
    matriz.append(list(map(int,input().split())))

print(matriz)
