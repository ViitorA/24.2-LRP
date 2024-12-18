nParticipantes = int(input())
contador = 0

while True:
    if nParticipantes != 0:
        contador += 1
        ingressos = list(map(int,input().split()))

        print("Teste",contador)
        for i in range(len(ingressos)):
            if ingressos[i] == i+1:
                print(ingressos[i])
                print()
        
        nParticipantes = int(input())
    else:
        break