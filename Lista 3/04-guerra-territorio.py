a = int(input())
comprimento = list(map(int,input().split()))
igual = 0

for n in comprimento:
    igual += n

igual = igual/2
indice = -1

n = 0
for i in range(len(comprimento)):
    n += comprimento[i]
    if n == igual:
        indice = i+1

print(indice)
