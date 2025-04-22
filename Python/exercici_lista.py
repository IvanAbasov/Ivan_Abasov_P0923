noms=[]
para = True

for nom in noms:
    print(nom)

    

while para:
    print("1-Intrud nomes")
    print("2-Listar nomes na lista")
    print("3-Parar Progama")

    dec = int(input(": "))
    
    if dec == 1:
        noms.append(input("Introduzir nome: "))

    elif dec == 2:
        print("Nomes na lista: ")
        for nom in noms:
            print(nom)

    elif dec == 3:
        para = False

    else:
        print("Opção incorreta")
