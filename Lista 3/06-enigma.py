cifrada = input()
crib = input()

possiveis = 0

for i in range(len(cifrada)-len(crib)+1):
    naoDa = False
    for j in range(len(crib)): 
        if cifrada[i+j] == crib[j]: 
            naoDa = True
            break
        
    if not naoDa: possiveis += 1

print(possiveis)
