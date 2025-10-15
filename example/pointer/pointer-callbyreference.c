#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void main() {
    int num1 = 100;
    int num2 = 200;

    printf("교환 전, num1 = %d, num2 = %d\n", num1, num2);

    swap(&num1, &num2); // 주소를 전달

    printf("교환 후, num1 = %d, num2 = %d\n", num1, num2);
}