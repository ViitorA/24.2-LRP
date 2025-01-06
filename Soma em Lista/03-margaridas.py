# l -> n linhas
# c -> n colunas
# m -> n linhas lote
# n -> n colunas lote
l,c,m,n = map(int,input().split())

matriz = []

for i in range(l):
    matriz.append(list(map(int,input().split())))

maior_soma = 0
for i in range(0,l,m):
    for j in range(0,c,n):
        soma = 0
        for k in range(m):
            for l in range(n):
                soma += matriz[k+i][l+j]
        maior_soma = max(soma,maior_soma)

print(maior_soma)
