#include <stdio.h>
#include <stdlib.h>

int main() {
    int *p_arr;
    int n = 5;

    // 정수 n개를 저장할 수 있는 메모리 공간을 동적으로 할당
    // (int*)는 타입 캐스팅, malloc이 반환한 주소를 이 주소로부터 시작하는 공간은 int 타입의 데이터를 저장하는 데 쓸 것이라는 걸 명확히 함 
    p_arr = (int*)malloc(sizeof(int)*n);

    if (p_arr == NULL) {
        printf("메모리 할당 오류\n");
        return 1;
    }

    for (int i=0; i<n; i++) {
        p_arr[i] = (i+1)*10;
    }

    for (int i=0; i<n; i++) {
        printf("%d ", p_arr[i]);
    }
    
    free(p_arr);
}