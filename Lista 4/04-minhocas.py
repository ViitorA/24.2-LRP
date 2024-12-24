# Meu Deus, que código horroroso

linhas,colunas = map(int,input().split())
campo = []
somatoria_linhas = [0]*linhas
somatoria_colunas = [0]*colunas
mais_produtivas = [0]*2

#  Coloca os valores do input na matriz do campo
for i in range(linhas):
    campo.append(list(map(int,input().split())))

# Vê a somatória das linhas
for i in range(linhas):
    for j in range(colunas):
        somatoria_linhas[i] += campo[i][j]

# Vê a somatória das colunas
for i in range(colunas):
    for j in range(linhas):
        somatoria_colunas[i] += campo[j][i]

# Verifica qual linha ou coluna é a mais produtiva
mais_produtivas[0] = max(somatoria_linhas)
mais_produtivas[1] = max(somatoria_colunas)

print(max(mais_produtivas))
