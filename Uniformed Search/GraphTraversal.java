import java.util.*;

public class GraphTraversal {
    private int V; // number of vertices
    private LinkedList<Integer>[] adj; // adjacency list

    public GraphTraversal(int v) {
        V = v;
        adj = new LinkedList[v];
        for (int i = 0; i < v; i++) {
            adj[i] = new LinkedList<>();
        }
    }

    // add an edge to the graph
    public void addEdge(int v, int w) {
        adj[v].add(w);
    }

    // Depth-First Search
    public void DFS(int v) {
        boolean[] visited = new boolean[V];
        DFSUtil(v, visited);
    }

    private void DFSUtil(int v, boolean[] visited) {
        visited[v] = true;
        System.out.print(v + " ");

        for (int n : adj[v]) {
            if (!visited[n]) {
                DFSUtil(n, visited);
            }
        }
    }

    // Breadth-First Search
    public void BFS(int v) {
        boolean[] visited = new boolean[V];
        LinkedList<Integer> queue = new LinkedList<>();

        visited[v] = true;
        queue.add(v);

        while (queue.size() != 0) {
            v = queue.poll();
            System.out.print(v + " ");

            for (int n : adj[v]) {
                if (!visited[n]) {
                    visited[n] = true;
                    queue.add(n);
                }
            }
        }
    }

    // Uniform-Cost Search
    public void UCS(int start, int end) {
        PriorityQueue<Node> pq = new PriorityQueue<>(new Comparator<Node>() {
            @Override
            public int compare(Node o1, Node o2) {
                return o1.cost - o2.cost;
            }
        });

        pq.add(new Node(start, 0, null));
        HashSet<Integer> visited = new HashSet<>();

        while (!pq.isEmpty()) {
            Node curr = pq.poll();

            if (curr.vertex == end) {
                printPath(curr);
                return;
            }

            if (visited.contains(curr.vertex))
                continue;

            visited.add(curr.vertex);

            for (int v : adj[curr.vertex]) {
                if (!visited.contains(v)) {
                    pq.add(new Node(v, curr.cost + 1, curr));
                }
            }
        }
    }

    private void printPath(Node node) {
        if (node == null) {
            return;
        }

        printPath(node.parent);
        System.out.print(node.vertex + " ");
    }

    private class Node {
        int vertex;
        int cost;
        Node parent;

        public Node(int v, int c, Node p) {
            vertex = v;
            cost = c;
            parent = p;
        }
    }

    // driver code
    public static void main(String[] args) {
        GraphTraversal g = new GraphTraversal(4);

        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 0);
        g.addEdge(2, 3);
        // g.addEdge(3, 3);

        System.out.println("Depth-First Search:");
        g.DFS(2);

        System.out.println("\nBreadth-First Search:");
        g.BFS(2);

        System.out.println("\nUniform-Cost Search:");
        g.UCS(0, 3);
    }
}
