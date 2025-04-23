#include <stdio.h>

int main() {
    char nome[50];
    float preco = 0;
    float desconto, valorFinal;

    printf("Escreve o teu nome: ");
    scanf("%s", nome);

    printf("Valor da compra: ");
    scanf("%f", &preco);
    

    if (preco <= 200) {
        desconto = preco * 0.1; 
    } else if (preco <= 500) {
        desconto = preco * 0.15; 
    } else {
        desconto = preco * 0.2; 
    }

    valorFinal = preco - desconto; 

    
    printf("\nNome do cliente: %s\n", nome);
    printf("Valor da compra: %.2f€\n", preco);
    printf("Percentual de desconto: %.0f%%\n", (desconto / preco) * 100);
    printf("Valor do desconto: %.2f€\n", desconto);
    printf("Valor total a pagar: %.2f€\n", valorFinal);

    return 0;
}