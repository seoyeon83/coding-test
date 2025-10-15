#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_SIZE 100

// 원형 큐
typedef struct {
    int data[MAX_SIZE];
    int front;
    int rear;
    int size;
} CircularQueue;

// 큐 초기화
void initQueue(CircularQueue *queue) {
    queue->front = 0;
    queue->rear = -1;
    queue->size = 0;
}

// 큐가 비어있는지 확인
bool isEmpty(CircularQueue *queue) {
    return queue->size == 0;
}

// 큐가 가득 찼는지 확인
bool isFull(CircularQueue *queue) {
    return queue->size == MAX_SIZE;
}

// enqueue 연산
void enqueue(CircularQueue *queue, int value) {
    if (isFull(queue)) {
        printf("큐 오버플로우! 큐가 가득 찼습니다.\n");
        return;
    }
    queue->rear = (queue->rear + 1) % MAX_SIZE;
    queue->data[queue->rear] = value;
    queue->size++;
    printf("%d를 enqueue했습니다.\n", value);
}

// dequeue 연산
int dequeue(CircularQueue *queue) {
    if (isEmpty(queue)) {
        printf("큐 언더플로우! 큐가 비어있습니다.\n");
        return -1;
    }
    int value = queue->data[queue->front];
    queue->front = (queue->front + 1) % MAX_SIZE;
    queue->size--;
    return value;
}

// front 요소 확인
int peek(CircularQueue *queue) {
    if (isEmpty(queue)) {
        printf("큐가 비어있습니다.\n");
        return -1;
    }
    return queue->data[queue->front];
}

// 큐 크기
int queueSize(CircularQueue *queue) {
    return queue->size;
}

// 큐 출력
void printQueue(CircularQueue *queue) {
    if (isEmpty(queue)) {
        printf("큐가 비어있습니다.\n");
        return;
    }
    printf("큐 내용 (front->rear): ");
    for (int i = 0; i < queue->size; i++) {
        int index = (queue->front + i) % MAX_SIZE;
        printf("%d ", queue->data[index]);
    }
    printf("\n");
}

// 연결 리스트 기반 큐
typedef struct QueueNode {
    int data;
    struct QueueNode *next;
} QueueNode;

typedef struct {
    QueueNode *front;
    QueueNode *rear;
    int size;
} LinkedQueue;

// 연결 큐 초기화
void initLinkedQueue(LinkedQueue *queue) {
    queue->front = NULL;
    queue->rear = NULL;
    queue->size = 0;
}

// 연결 큐 enqueue
void linkedEnqueue(LinkedQueue *queue, int value) {
    QueueNode *newNode = (QueueNode*)malloc(sizeof(QueueNode));
    newNode->data = value;
    newNode->next = NULL;
    
    if (queue->rear == NULL) {
        queue->front = queue->rear = newNode;
    } else {
        queue->rear->next = newNode;
        queue->rear = newNode;
    }
    queue->size++;
    printf("%d를 enqueue했습니다.\n", value);
}

// 연결 큐 dequeue
int linkedDequeue(LinkedQueue *queue) {
    if (queue->front == NULL) {
        printf("큐가 비어있습니다.\n");
        return -1;
    }
    QueueNode *temp = queue->front;
    int value = temp->data;
    queue->front = temp->next;
    
    if (queue->front == NULL) {
        queue->rear = NULL;
    }
    
    free(temp);
    queue->size--;
    return value;
}

// 연결 큐 출력
void printLinkedQueue(LinkedQueue *queue) {
    if (queue->front == NULL) {
        printf("큐가 비어있습니다.\n");
        return;
    }
    printf("연결 큐 (front->rear): ");
    QueueNode *temp = queue->front;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

// 연결 큐 메모리 해제
void freeLinkedQueue(LinkedQueue *queue) {
    while (queue->front != NULL) {
        linkedDequeue(queue);
    }
}

int main() {
    printf("=== 원형 큐 예제 ===\n\n");
    
    CircularQueue queue;
    initQueue(&queue);
    
    enqueue(&queue, 10);
    enqueue(&queue, 20);
    enqueue(&queue, 30);
    enqueue(&queue, 40);
    printQueue(&queue);
    
    printf("Front 요소: %d\n", peek(&queue));
    printf("큐 크기: %d\n", queueSize(&queue));
    
    printf("Dequeue: %d\n", dequeue(&queue));
    printf("Dequeue: %d\n", dequeue(&queue));
    printQueue(&queue);
    
    enqueue(&queue, 50);
    enqueue(&queue, 60);
    printQueue(&queue);
    
    printf("\n=== 연결 리스트 기반 큐 예제 ===\n\n");
    
    LinkedQueue linkedQueue;
    initLinkedQueue(&linkedQueue);
    
    linkedEnqueue(&linkedQueue, 100);
    linkedEnqueue(&linkedQueue, 200);
    linkedEnqueue(&linkedQueue, 300);
    printLinkedQueue(&linkedQueue);
    
    printf("Dequeue: %d\n", linkedDequeue(&linkedQueue));
    printLinkedQueue(&linkedQueue);
    
    freeLinkedQueue(&linkedQueue);
    
    return 0;
}