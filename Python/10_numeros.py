num = []

print("Escreve 10 numeros\n")

for i in range (10):
    numero = int(input("Escreve um numero: "))
    if numero % 2 == 0:
        num.append(numero)

print(num)