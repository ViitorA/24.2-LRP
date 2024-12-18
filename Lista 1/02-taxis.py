# preço alcool, preço gasolina, km/litro em cada um
# caso preço alcool=gasolina, use gasolina

# entradas [Preço Alcool, Preço Gasolina, rendimento km/l alcool, rendimento km/l gasolina]
entradas = list(map(float, input().split()))

if entradas[2]/entradas[0] > entradas[3]/entradas[1]:
    print('A')
else:
    print('G')
