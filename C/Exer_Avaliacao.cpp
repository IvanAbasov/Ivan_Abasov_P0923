#include <stdio.h>

int main() {
    int notas[10];
    float soma = 0;
    int alunosAcimaDaMedia = 0;


    for (int i = 0; i < 10; i++) {
        printf("Escreva a nota do aluno %d (0 a 20): ", i + 1);
        scanf("%d", &notas[i]);

 
        while (notas[i] < 0 || notas[i] > 20) {
            printf("Nota inválida! Por favor, insira uma nota entre 0 e 20: ");
            scanf("%d", &notas[i]);
        }

        soma += notas[i];
    }


    float media = soma / 10;


    printf("Média das notas: %.2f\n", media);


    for (int i = 0; i < 10; i++) {
        if (notas[i] >= media) {
            alunosAcimaDaMedia++;
        }
    }


    printf("Número de alunos com notas iguais ou acima da média: %d\n", alunosAcimaDaMedia);

    return 0;
}
