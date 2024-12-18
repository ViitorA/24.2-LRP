# L = Linhas do Tabuleiro
# C = Colunas do Tabuleiro
L = int(input()) # 1 <= L <= 1000
C = int(input()) # 1 <= C <= 1000

# 0 = Casa Preta
# 1 = Casa Branca

print(1) if (L+C)%2 == 0 else print(0)
