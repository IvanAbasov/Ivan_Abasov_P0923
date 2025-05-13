def obter_numero_par():
    while True:
        try:
            numero = int(input("Digite um número par entre 1 e 50: "))
            if numero < 1 or numero > 50:
                print("O número deve estar entre 1 e 50.")
            elif numero % 2 != 0:
                print("O número deve ser par.")
            else:
                return numero
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

def calcular_media():
    soma = 0
    for i in range(30):
        print(f"Digite o {i + 1}º número:")
        numero = obter_numero_par()
        soma += numero
    
    media = soma / 30
    print(f"A média dos 30 números é: {media}")


calcular_media()
