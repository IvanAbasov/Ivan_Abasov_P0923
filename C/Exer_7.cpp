#include <stdio.h>

int main() {
    float nota1= 0;
    float nota2 = 0;
    float nota3 = 0;
    float media;

 
    printf("Digite a nota da primeira prova (0 a 10): ");
    scanf("%f", &nota1);

    printf("Digite a nota da segunda prova (0 a 10): ");
    scanf("%f", &nota2);

    printf("Digite a nota da terceira prova (0 a 10): ");
    scanf("%f", &nota3);


    media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / (2 + 3 + 5);


    printf("Média final: %.2f\n", media);

    if (media >= 6) {
        printf("APROVADO\n");
    } else {
        printf("REPROVADO\n");
    }

    return 0;
}
