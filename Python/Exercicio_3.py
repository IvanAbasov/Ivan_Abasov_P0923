print("Escreve 10 notas\n")

soma = 0  

for i in range(10):
    nota = int(input("Escreve nota: "))
    soma += nota  

media = soma / 10  
print(f"A média das notas dos alunos é {media}")
