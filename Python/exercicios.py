num1 = input("Escreve o num1: ")
num2 = input("\nEscreve o num2: ")
num3 = input("\nEscreve o num3: ")


if num1>num2 and num2>num3:
    print("Num1 ser maior Num2 ser meio Num3 ser menor")

elif num1>num3 and num3>num2:
    print("Num1 ser maior Num3 ser meio Num2 ser menor")
elif num3>num2 and num2>num1:
    print("Num3 ser maior Num2 ser meio Num1 ser menor")
elif num3>num1 and num1>num2:
    print("Num3 ser maior Num1 ser meio Num2 ser menor")
elif num2>num1 and num1>num3:
    print("Num2 ser maior Num1 ser meio Num3 ser menor")
elif num2>num3 and num3>num1:
    print("Num2 ser maior Num3 ser meio Num1 ser menor")
else:
    print("Numero iguais")