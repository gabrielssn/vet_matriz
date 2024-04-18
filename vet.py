def verificar_repetidos(vetor):
    numeros_repetidos = {}
    for i, num in enumerate(vetor):
        if num in numeros_repetidos:
            numeros_repetidos[num].append(i)
        else:
            numeros_repetidos[num] = [i]

    repetidos_encontrados = False
    for num, posicoes in numeros_repetidos.items():
        if len(posicoes) > 1:
            print(f"O número {num} está repetido nas posições:", posicoes)
            repetidos_encontrados = True

    if not repetidos_encontrados:
        print("Não foram encontrados números repetidos no vetor.")


VET = []
print("Digite 10 números:")
for _ in range(10):
    numero = int(input())
    VET.append(numero)

verificar_repetidos(VET)