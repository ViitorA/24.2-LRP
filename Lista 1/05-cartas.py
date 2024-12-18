cartas = list(map(int, input().split()))
crescente = True
decrescente = True

for c in range(len(cartas)-1):
    if cartas[c] < cartas[c+1]:
        crescente = True
    else:
        crescente = False
        break
    
for d in range(len(cartas)-1,0,-1):
    if cartas[d] < cartas[d-1]:
        decrescente = True
    else:
        decrescente = False
        break

if crescente and not decrescente:
    print('C')
elif not crescente and decrescente:
    print('D')
else:
    print('N')
