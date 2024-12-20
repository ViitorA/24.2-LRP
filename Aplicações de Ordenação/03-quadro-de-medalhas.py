def ordenar(paises):
    return -paises[1],-paises[2],-paises[3],paises[0]

nP = int(input())
paises = []

for p in range(nP):
    paises.append(list(input().split()))
    for i in range(1,4):
        paises[p][i] = int(paises[p][i])

paises.sort(reverse=False,key=ordenar)

for i in range(len(paises)):
    print(f"{paises[i][0]} {paises[i][1]} {paises[i][2]} {paises[i][3]}")