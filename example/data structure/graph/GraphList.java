import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class GraphList {
    private Map<Integer, List<Integer>> adjList;

    public GraphList() {
        this.adjList = new HashMap<>();
    }

    // 정점 추가
    public void addVertex(int vertex) {
        adjList.putIfAbsent(vertex, new ArrayList<>());
    }

    // 간선 추가 (무방향)
    public void addEdge(int u, int v) {
        // 두 정점이 모두 존재하는지 확인하고 없으면 추가
        addVertex(u);
        addVertex(v);
        
        adjList.get(u).add(v);
        adjList.get(v).add(u);
    }

    public void printGraph() {
        System.out.println("인접 리스트:");
        for (Integer vertex : adjList.keySet()) {
            System.out.print("정점 " + vertex + " -> ");
            System.out.println(adjList.get(vertex));
        }
    }
    
    public static void main(String[] args) {
        GraphList g = new GraphList();
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 3);
        g.printGraph();
    }
}