nRodadas = int(input())

while True:
    if nRodadas != 0:
        pA,pB = 0,0

        for i in range(nRodadas):
            A,B = map(int,input().split())
            if A > B:
                pA += 1
            elif A < B:
                pB += 1

        print(pA,pB)
        nRodadas = int(input())
    else:
        break