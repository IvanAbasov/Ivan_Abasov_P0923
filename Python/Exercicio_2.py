num = []
impar= []

print("Escreve 10 numeros\n")

for i in range (10):
    numero = int(input("Escreve um numero: "))
    if numero % 2 == 0:
        num.append(numero)
    else:
        impar.append(numero)

print(num)
print(impar)