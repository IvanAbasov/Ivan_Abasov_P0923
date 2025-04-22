opc=0


print("Bem Vindo")
print(" prima 1 para nome cliente")
print("Prima 2 para Iban")
opc = input("Intrud opçao: ")

match opc:
    case 1:
        print("Nome")

    case 2:
        print("Iban")


    case default:
        print("Falhou")
if opc == 1:
    print("Nome")
elif opc == 2:
    print("Iban")
else:
    print("Nao existe")