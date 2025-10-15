/*
pointer: 다른 변수의 메모리 주소를 저장하는 특별한 변수
&: 주소연산자, 변수 앞에 붙여 해당 변수의 메모리 주소를 가져온다
*: 참조연산자, 포인터변수 앞에 붙여서 포인터가 가리키는 주소에 저장된 실제 값에 접근한다 (역참조)

변수가 집이라면, &는 주소를 알려주는 것, *는 주소를 따라 집에 찾아가는 것
&는 무조건 변수 앞에 붙어서 그 변수가 저장된 메모리 주소를 반환
int *p => p는 포인터 변수다
*p = 20 or printf("%d", *p) => 이 포인터가 가리키는 주소로 가서 값을 가져오거나 바꿔라 (역참조)

*/

#include <stdio.h>

int main() {
    int num = 10;
    int *p_num;

    p_num = &num; // num의 메모리 주소

    printf("num = %d\n", num);
    printf("&num = %p\n", &num);
    printf("p_num = %p\n", p_num);
    printf("*p_num = %d\n", *p_num);

    *p_num = 20;
    printf("*p_num = 20 으로 값 변경 후 num = %d\n", num);

    printf("\n");

    // int age;
    // printf("나이를 입력하세요: ");
    // scanf("%d", &age); // age 변수의 주소에 값을 넣어라
    // printf("\n나이 = %d", age);

    // printf("\n");

    return 0; 
}