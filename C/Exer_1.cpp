#include <stdio.h>

int main(){
    int h;
    int horas = h / 3600; 

    int minutos = h / 60;

    printf("Escreve o tempo em segundos: ");
    scanf("%d",&h);

    printf("A converter para horas fica %d, para minutos fica %d, e segundos fica %d", horas, minutos, h);

}
