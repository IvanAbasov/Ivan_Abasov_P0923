pares = []
impares = []


for i in range(1, 61):  
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)


print("Os 30 primeiros números pares são:")
print(pares)  

print("\nOs 30 primeiros números ímpares são:")
print(impares) 
