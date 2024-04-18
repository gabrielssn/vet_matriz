import random

matriz_A = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]

print("Matriz A:")
for linha in matriz_A:
    print(linha)

soma_A = sum(sum(linha) for linha in matriz_A)
print("\nA soma de todos os valores da matriz A é:", soma_A)

matriz_B = [[elemento * 3 for elemento in linha] for linha in matriz_A]


print("\nMatriz B (valores de A multiplicados por 3):")
for linha in matriz_B:
    print(linha)