contador_operacoes = 0

numero = int(input("Digite um número: "))


for i in range(1, numero): 

    soma = numero + i
    print(f"{numero} + {i} = {soma}")
    contador_operacoes += 1  

    subtracao = numero - i
    print(f"{numero} - {i} = {subtracao}")
    contador_operacoes += 1  

    multiplicacao = numero * i
    print(f"{numero} * {i} = {multiplicacao}")
    contador_operacoes += 1 

    if i != 0:
        divisao = numero / i
        print(f"{numero} / {i} = {divisao:.2f}")
        contador_operacoes += 1  

print(f"\nTotal de operações realizadas: {contador_operacoes}")
