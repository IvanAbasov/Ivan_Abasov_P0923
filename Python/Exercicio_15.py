def mostrar_ascii():
    for i in range(0, 256, 20):
        print("\n--- Códigos ASCII de", i, "a", min(i + 19, 255), "---")
        for j in range(i, min(i + 20, 256)):
            try:
                char = chr(j)
        
                if char.isspace():
                    char_repr = repr(char)
                elif char.isprintable():
                    char_repr = char
                else:
                    char_repr = "N/A"
            except:
                char_repr = "Erro"
            print(f"Código {j:3} -> Caractere: {char_repr}")
        

        resposta = input("\nDeseja continuar? (S/N): ").strip().lower()
        if resposta != 's':
            print("Programa encerrado.")
            break

mostrar_ascii()
