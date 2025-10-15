#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_SIZE 100

typedef struct {
    int data[MAX_SIZE];
    int top;
} Stack;

void init(Stack *stack) {
    stack->top = -1;
}

bool isEmpty(Stack *stack) {
    return stack->top == -1;
}

bool isFull(Stack *stack) {
    return stack->top == MAX_SIZE - 1;
}

void push(Stack *stack, int value) {
    if (isFull(stack)) {
        printf("overflow");
        return;
    }

    stack->data[++stack->top] = value;
}

int pop(Stack *stack) {
    if (isEmpty(stack)) {
        printf("underflow");
        return -1;
    }
    return stack->data[stack->top--];
}

int peek(Stack *stack) {
    if (isEmpty(stack)) {
        printf("stack is empty\n");
        return -1;
    }
    return stack->data[stack->top];
}

int size(Stack *stack) {
    return stack->top + 1;
}

void printStack(Stack *stack) {
    if (isEmpty(stack)) {
        printf("stack is empty\n");
        return;
    }
    printf("스택 내용 (top->bottom): ");
    for (int i=stack->top; i>=0; i--) {
        printf("%d ", stack->data[i]);
    }
    printf("\n");
}

int main() {
    Stack stack;
    init(&stack);

    push(&stack, 10);
    push(&stack, 20);
    push(&stack, 30);
    push(&stack, 40);
    printStack(&stack);

    printf("top = %d\n", peek(&stack));
    printf("size = %d\n", size(&stack));

    printf("pop = %d\n", pop(&stack));
    printf("pop = %d\n", pop(&stack));
    printStack(&stack);
}