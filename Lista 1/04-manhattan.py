# Coordenadas Maria   = (Xm,Ym)
# Coordenadas Reunião = (Xr,Yr)
# entrada = [Xm, Ym, Xr, Yr]
entrada = list(map(int,input().split()))

print(abs(entrada[0]-entrada[2])+abs(entrada[1]-entrada[3]))
