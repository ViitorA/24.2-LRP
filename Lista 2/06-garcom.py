bandejas = int(input())
coposQuebrados = 0

for i in range(bandejas):
    L,C = map(int,input().split())

    if L>C: coposQuebrados += C

print(coposQuebrados)
