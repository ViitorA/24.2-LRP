numero_testes = int(input())

for i in range(numero_testes):
    posicao = 0
    num_instrucoes = int(input())
    instrucoes = []
    for j in range(num_instrucoes):
        entrada = input()
        if entrada == "LEFT":
            instrucoes.append(entrada)
            posicao -= 1
        elif entrada == "RIGHT":
            instrucoes.append(entrada)
            posicao += 1
        else:
            entrada = list(entrada.split())
            if instrucoes[int(entrada[-1])-1] == "LEFT":
                instrucoes.append("LEFT")
                posicao -= 1
            else:
                instrucoes.append("RIGHT")
                posicao += 1
    print(posicao)
