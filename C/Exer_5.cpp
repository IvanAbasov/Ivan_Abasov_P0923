#include <stdio.h>

int main(){

    int num1 = 0;
    int num2 = 0;
    int num3 = 0;
 
    printf("Escreve tres numeros: ");
    scanf("%d %d %d", &num1, &num2, &num3);

    printf("Crescente: ");
   if (num1 <= num2 && num1 <= num3 ) {

        printf("%d ", num1);
        if (num2 <= num3) {
            printf("%d %d ", num2, num3);
        }else{

            printf("%d %d ",num3, num2);

        }
   }else if (num2 <= num1 && num2 <= num3){

        printf("%d ",num2);
        if(num1 <= num3){
            printf("%d %d ", num1, num3);
        }else{

            printf("%d %d ", num3, num1);

        }

   }else{

        printf("%d ",num3);
        if(num1 <= num2) {
            printf("%d %d ", num1, num2);
        }else{

            printf("%d %d ",num2, num1);

        }

   }



   printf("Decrescente: ");
    for (int i = 0; i < 3; i++) {
        if (i == 0) {
            if (num1 >= num2 && num1 >= num3) {
                printf("%d ", num1);
                if (num2 >= num3) {
                    printf("%d %d\n", num2, num3);
                } else {
                    printf("%d %d\n", num3, num2);
                }
            } else if (num2 >= num1 && num2 >= num3) {
                printf("%d ", num2);
                if (num1 >= num3) {
                    printf("%d %d\n", num1, num3);
                } else {
                    printf("%d %d\n", num3, num1);
                }
            } else {
                printf("%d ", num3);
                if (num1 >= num2) {
                    printf("%d %d\n", num1, num2);
                } else {
                    printf("%d %d\n", num2, num1);
                }
            }
        }
    }

    return 0;
}
