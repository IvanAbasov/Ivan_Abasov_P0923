contagem_divisores = 0

numero = int(input("Digite um número: "))



for i in range(1, numero + 1):  
    if numero % i == 0:  
        contagem_divisores += 1  


print(f"O número {numero} possui {contagem_divisores} divisores.")
