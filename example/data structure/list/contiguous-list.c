// 연속 리스트

#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int* data;
    int size;     // 크기(몇개의 값이 들어있는지)
    int capacity; // 용량
} ContiguousList;

void init(ContiguousList* list, int capacity) {
    list->data = (int*)malloc(capacity * sizeof(int));
    list->size = 0;
    list->capacity = capacity;
}

void append(ContiguousList* list, int value) {
    // 필요시 메모리 재할당
    // realloc은 이미 할당한 공간의 크기를 바꿀 때 사용 (용량 2배로)
    // realloc(이미 할당한 포인터 변수, 바꾸고 싶은 공간의 크기)
    if(list->size == list->capacity) {
        list->capacity *= 2;
        list->data = (int*)realloc(list->data, list->capacity * sizeof(int));
    }
    list->data[list->size++] = value;
    printf("용량 = %d, 크기 = %d\n", list->capacity, list->size);
}

int main() {
    ContiguousList myList;
    init(&myList, 2);

    append(&myList, 10);
    append(&myList, 20);
    append(&myList, 30);

    for (int i=0; i<myList.size; i++) {
        printf("myList.data[i] = %d\n", myList.data[i]);
    }

    printf("용량 = %d, 크기 = %d\n", myList.capacity, myList.size);
    free(myList.data);

    return 0;
}