risada = list(input())

vogais = ['a','e','i','o','u']
vogais_ida = []
for vogal in risada:
    if vogal in vogais: vogais_ida.append(vogal)

vogais_volta = vogais_ida[::-1]

print('S') if vogais_ida == vogais_volta else print('N')
