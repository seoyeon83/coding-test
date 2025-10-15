#include <stdio.h>

int main() {
    int arr[5] = {10, 20, 30, 40, 50};
    int *p_arr = arr;     // arr = &arr[0] (arr[0]의 주소)

    printf("arr = &arr[0]\n");
    printf("arr = %p\n", arr);
    printf("&arr[0] = %p\n", &arr[0]);

    printf("\n");

    printf("p_arr = %p\n", p_arr);
    printf("*p_arr = %d\n", *p_arr);

    for(int i=0; i<5; i++) {
        printf("*(p_arr+%d) = %d\n", i, *(p_arr+i));
    }
}