/*
이중 포인터:
포인터 자체도 변수이므로 그 자체로도 주소를 가진다. 이 포인터의 주소를 저장하는 것
*/

#include <stdio.h>

int main() {
    int num = 123;
    int *p_num;
    int **pp_num;

    p_num = &num;
    pp_num = &p_num;

    printf("num = %d\n", num);
    printf("*p_num = %d\n", *p_num);
    printf("**p_num = %d\n", **pp_num);

    printf("\n");
    printf("&num = p_num = %p\n", &num);
    printf("&num = p_num = %p\n", p_num);
    
    printf("&p_num = pp_num = %p\n", &p_num);
    printf("&p_num = pp_num = %p\n", pp_num);

    
    printf("&pp_num = %p\n", &pp_num);
}