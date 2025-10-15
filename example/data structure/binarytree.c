#include <stdio.h>
#include <stdlib.h>

// 트리의 기본 단위인 노드 구조체 정의
typedef struct Node {
    int data;
    struct Node* left;
    struct Node* right;
} Node;

// 새로운 노드를 생성하는 함수
Node* createNode(int value) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL) {
        printf("메모리 할당 오류!\n");
        exit(1);
    }
    newNode->data = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// -------------------- 추가 (Insertion) --------------------
// 이진 탐색 트리에 노드를 추가하는 함수 (재귀 방식)
Node* insert(Node* root, int data) {
    // 트리가 비어있으면, 새로운 노드를 루트로 반환
    if (root == NULL) {
        return createNode(data);
    }

    // 삽입할 데이터가 현재 노드보다 작으면 왼쪽 서브트리로 이동
    if (data < root->data) {
        root->left = insert(root->left, data);
    }
    // 삽입할 데이터가 현재 노드보다 크면 오른쪽 서브트리로 이동
    else if (data > root->data) {
        root->right = insert(root->right, data);
    }

    // (데이터가 같은 경우 삽입하지 않음)
    return root;
}


// -------------------- 순회 (Traversal) --------------------
// 1. 전위 순회 (Pre-order: Root -> Left -> Right)
void printPreorder(Node* root) {
    if (root != NULL) {
        printf("%d ", root->data); // 루트 노드 방문
        printPreorder(root->left); // 왼쪽 서브트리 순회
        printPreorder(root->right); // 오른쪽 서브트리 순회
    }
}

// 2. 중위 순회 (In-order: Left -> Root -> Right)
// (이진 탐색 트리에서 중위 순회는 정렬된 결과를 출력합니다)
void printInorder(Node* root) {
    if (root != NULL) {
        printInorder(root->left);  // 왼쪽 서브트리 순회
        printf("%d ", root->data);  // 루트 노드 방문
        printInorder(root->right); // 오른쪽 서브트리 순회
    }
}

// 3. 후위 순회 (Post-order: Left -> Right -> Root)
void printPostorder(Node* root) {
    if (root != NULL) {
        printPostorder(root->left);  // 왼쪽 서브트리 순회
        printPostorder(root->right); // 오른쪽 서브트리 순회
        printf("%d ", root->data);   // 루트 노드 방문
    }
}


// -------------------- 삭제 (Deletion) --------------------
// 특정 서브트리에서 가장 작은 값을 가진 노드를 찾는 함수
Node* findMinValueNode(Node* node) {
    Node* current = node;
    // 가장 왼쪽 끝에 있는 노드가 최솟값
    while (current && current->left != NULL) {
        current = current->left;
    }
    return current;
}

// 이진 탐색 트리에서 노드를 삭제하는 함수
Node* deleteNode(Node* root, int data) {
    if (root == NULL) return root;

    // 삭제할 데이터가 현재 노드보다 작으면 왼쪽으로 이동
    if (data < root->data) {
        root->left = deleteNode(root->left, data);
    }
    // 삭제할 데이터가 현재 노드보다 크면 오른쪽으로 이동
    else if (data > root->data) {
        root->right = deleteNode(root->right, data);
    }
    // 삭제할 데이터를 찾았을 경우
    else {
        // 경우 1: 자식 노드가 없거나 하나만 있는 경우
        if (root->left == NULL) {
            Node* temp = root->right;
            free(root);
            return temp;
        } else if (root->right == NULL) {
            Node* temp = root->left;
            free(root);
            return temp;
        }

        // 경우 2: 자식 노드가 둘 다 있는 경우
        // 오른쪽 서브트리에서 가장 작은 노드(in-order successor)를 찾음
        Node* temp = findMinValueNode(root->right);

        // 찾은 successor의 데이터를 현재 노드에 복사
        root->data = temp->data;

        // 원래 successor가 있던 자리의 노드를 삭제
        root->right = deleteNode(root->right, temp->data);
    }
    return root;
}


// -------------------- 메인 함수 --------------------
int main() {
    Node* root = NULL;

    // 1. 노드 추가
    printf("--- 1. 노드 추가 ---\n");
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 20);
    insert(root, 40);
    insert(root, 70);
    insert(root, 60);
    insert(root, 80);

    // 2. 순회 결과 출력
    printf("\n--- 2. 초기 순회 결과 ---\n");
    printf("전위 순회 (Pre-order): ");
    printPreorder(root);
    printf("\n");

    printf("중위 순회 (In-order):  ");
    printInorder(root);
    printf("\n");

    printf("후위 순회 (Post-order): ");
    printPostorder(root);
    printf("\n");

    // 3. 노드 삭제
    printf("\n--- 3. 노드 삭제 ---\n");
    
    // Case 1: 자식이 없는 노드(20) 삭제
    printf("\n삭제할 노드: 20 (자식 없음)\n");
    root = deleteNode(root, 20);
    printf("중위 순회 결과: ");
    printInorder(root);
    printf("\n");

    // Case 2: 자식이 하나인 노드(30) 삭제
    printf("\n삭제할 노드: 30 (자식 하나)\n");
    root = deleteNode(root, 30);
    printf("중위 순회 결과: ");
    printInorder(root);
    printf("\n");
    
    // Case 3: 자식이 둘인 노드(50, 루트) 삭제
    printf("\n삭제할 노드: 50 (자식 둘)\n");
    root = deleteNode(root, 50);
    printf("중위 순회 결과: ");
    printInorder(root);
    printf("\n");
    
    // 4. 최종 순회 결과 출력
    printf("\n--- 4. 최종 순회 결과 ---\n");
    printf("전위 순회 (Pre-order): ");
    printPreorder(root);
    printf("\n");

    printf("중위 순회 (In-order):  ");
    printInorder(root);
    printf("\n");

    printf("후위 순회 (Post-order): ");
    printPostorder(root);
    printf("\n");

    // 메모리 해제는 생략 (실제 프로그램에서는 모든 노드를 순회하며 free 해야 함)
    return 0;
}