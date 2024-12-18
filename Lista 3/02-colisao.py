o1 = list(map(int,input().split()))
o2 = list(map(int,input().split()))
intersec = 1

if o1[1] > o2[3] or o1[3] < o2[1] or o1[2] < o2[0] or o1[0] > o2[2]:
    intersec = 0

print(intersec)
