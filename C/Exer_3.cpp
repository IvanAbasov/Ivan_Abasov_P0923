#include <stdio.h>

int main() {
    int num1 = 0;
    int num2 = 0;

 
    printf("Digite o primeiro numero: ");
    scanf("%d", &num1);

    printf("Digite o segundo numero: ");
    scanf("%d", &num2);


    if (num1 > num2) {
        printf("Decrescente: %d, %d\n", num1, num2);
    } else {
        printf("Decrescente: %d, %d\n", num2, num1);
    }

    return 0;
}
