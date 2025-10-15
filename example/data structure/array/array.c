#include <stdio.h>

int main() {
    int n[5] = {10, 20, 30, 40, 50};

    printf("n[0] = %d\n", n[0]);
    printf("n[4] = %d\n", n[4]);

    
    printf("n[1] = %d\n", n[1]);
    n[1] = 25;
    printf("n[1] = %d\n", n[1]);

    for (int i=0; i<sizeof(n); i++){
        printf("%d ", n[i]);
    }

    return 0;
}