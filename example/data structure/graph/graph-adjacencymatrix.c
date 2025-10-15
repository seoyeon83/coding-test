#include <stdio.h>
#define VERTICES 4

// 그래프 초기화 (0으로)
void initGraph(int adjMatrix[][VERTICES]) {
    for (int i = 0; i < VERTICES; i++) {
        for (int j = 0; j < VERTICES; j++) {
            adjMatrix[i][j] = 0;
        }
    }
}

// 간선 추가 (무방향 그래프)
void addEdge(int adjMatrix[][VERTICES], int u, int v) {
    adjMatrix[u][v] = 1;
    adjMatrix[v][u] = 1;
}

void printGraph(int adjMatrix[][VERTICES]) {
    for (int i = 0; i < VERTICES; i++) {
        for (int j = 0; j < VERTICES; j++) {
            printf("%d ", adjMatrix[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int adjMatrix[VERTICES][VERTICES];
    initGraph(adjMatrix);

    addEdge(adjMatrix, 0, 1);
    addEdge(adjMatrix, 0, 2);
    addEdge(adjMatrix, 1, 2);
    addEdge(adjMatrix, 2, 3);

    printGraph(adjMatrix);

    return 0;
}