nPostos,distIntMax = map(int,input().split())
pAgua = list(map(int,input().split()))
pAgua.append(42195)

for i in range(1,len(pAgua)):
    if pAgua[i]-pAgua[i-1] > distIntMax:
        print('N')
        exit()

print('S')
