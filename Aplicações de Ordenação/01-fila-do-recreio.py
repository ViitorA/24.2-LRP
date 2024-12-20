nCasos = int(input())

for i in range(nCasos):
    qtdIguais = 0
    nAlunos = int(input())
    notas = list(map(int,input().split()))
    notasOrd = sorted(notas)
    notasOrd.reverse()

    for j in range(nAlunos):
        if notas[j] == notasOrd[j]:
            qtdIguais += 1

    print(qtdIguais)