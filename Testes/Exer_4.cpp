#include <stdio.h>

int main(){

    float saldo;
    float cheque;

    printf("Escreve o saldo inicial: ");
    scanf("%f", &saldo);

    printf("Escreve o cheque inicial: ");
    scanf("%f", &cheque);

    if (cheque> saldo){

        printf("Cheque não pode ser descontado, saldo insuficiente");

    }else{

        saldo -= cheque;

        printf("Cheque descontado. Novo saldo %2.f", saldo);

    }

}
