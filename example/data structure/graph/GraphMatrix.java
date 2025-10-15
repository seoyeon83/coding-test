public class GraphMatrix {
    private int V; // 정점의 개수
    private int[][] adjMatrix; // 인접 행렬

    public GraphMatrix(int vertices) {
        this.V = vertices;
        adjMatrix = new int[V][V];
    }

    // 간선 추가 (무방향)
    public void addEdge(int u, int v) {
        adjMatrix[u][v] = 1;
        adjMatrix[v][u] = 1;
    }

    public void printGraph() {
        System.out.println("인접 행렬:");
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                System.out.print(adjMatrix[i][j] + " ");
            }
            System.out.println();
        }
    }
    
    public static void main(String[] args) {
        GraphMatrix g = new GraphMatrix(4);
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 3);
        g.printGraph();
    }
}