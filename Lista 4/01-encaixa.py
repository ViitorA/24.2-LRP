quantidade = int(input())

for i in range(quantidade):
    # Recebe duas strings e faz de cada uma uma lista
    a,b = map(list,input().split())
    a = a[-(len(b)):] # Remove todos os elementos de a, tirando os ultimos n elementos, com n sendo o tamanho da lista b
    
    if a == b:
        print("encaixa")
    else:
        print("nao encaixa")
