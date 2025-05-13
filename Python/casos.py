numeros=[1,2,4,8,10]
#index   0 1 2 3 4
opc=0
numcompar=0
stop=""
 
while True:
    print("1 - Listar")
    print("2 - Insert")
    print("3 - Delete")
    print("4 - Procura")
    print("5 - sair")
    opc=int(input("escolha a opc"))
    match opc:
        case 1:
            #listar lista
            for i in range(len(numeros)):
                print(numeros[i])
        case 2:        
            #insert na lista
            while True:
                numeros.append(int(input("Insert Number")))
                stop=input("Y / Yes para parar de introd")
                if stop == "Y" or stop == "Yes":
                    break
        case 3:
            #Delete da lista
            numeros.remove(int(input("intrud numero para remover")))
        case 4:
            #Procurar na lista
            numcompar=int(input("Numero para Procura "))
            for i in range(len(numeros)):
                if(numeros[i]==numcompar):
                    print("encontrei o seu numero ", numeros[i])
        case 5:
            break
        case _:
            print("errou a opcao")      