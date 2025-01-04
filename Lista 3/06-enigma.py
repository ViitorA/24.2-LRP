#cifrada = input()
#crib = input()

cifrada = "FDMLCRDMRALF"
crib = ['A','R','M','A','D','A']
possiveis = 0

print(cifrada)
for i in range(len(crib)):
    naoDa = False
    for j in range(len(crib)):
        print(crib)
        if cifrada[j] == crib[j]:
            naoDa = True
            break;
        else:
            print(cifrada[j],'!=',crib[j])
            print("+1")
            possiveis += 1;
        
    if i < 8: crib.insert(0,'0')
        
print(possiveis)


#FDMLCRDMRALF
#ARMADA
#0ARMADA
#00ARMADA
#000ARMADA
#0000ARMADA
#00000ARMADA
