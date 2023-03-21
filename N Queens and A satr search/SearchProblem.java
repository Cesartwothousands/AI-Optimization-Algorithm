import java.util.*;

public class SearchProblem {
    public static void main(String[] args) {
        int n = 6;
        int[][] edges = { { 1, 2 }, { 1, 3 }, { 1, 4 }, { 2, 4 }, { 2, 5 }, { 4, 5 }, { 3, 4 }, { 4, 6 } };
        int a = 1, b = 6;

        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 1; i <= n; i++) {
            graph.put(i, new ArrayList<>());
        }
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        System.out.println("BFS shortest path: " + bfs(graph, n, a, b));
        System.out.println("DFS path: " + dfs(graph, n, a, b));
    }

    public static int bfs(Map<Integer, List<Integer>> graph, int n, int a, int b) {
        boolean[] visited = new boolean[n + 1];
        int[] distance = new int[n + 1];
        Arrays.fill(distance, -1);
        Queue<Integer> queue = new LinkedList<>();

        visited[a] = true;
        distance[a] = 0;
        queue.add(a);

        while (!queue.isEmpty()) {
            int curr = queue.poll();
            for (int neighbor : graph.get(curr)) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    distance[neighbor] = distance[curr] + 1;
                    queue.add(neighbor);
                }
            }
        }

        return distance[b];
    }

    public static List<Integer> dfs(Map<Integer, List<Integer>> graph, int n, int a, int b) {
        boolean[] visited = new boolean[n + 1];
        List<Integer> path = new ArrayList<>();

        dfsUtil(graph, visited, a, b, path);

        return path;
    }

    public static boolean dfsUtil(Map<Integer, List<Integer>> graph, boolean[] visited, int curr, int b,
            List<Integer> path) {
        visited[curr] = true;
        path.add(curr);

        if (curr == b) {
            return true;
        }

        for (int neighbor : graph.get(curr)) {
            if (!visited[neighbor]) {
                if (dfsUtil(graph, visited, neighbor, b, path)) {
                    return true;
                }
            }
        }

        path.remove(path.size() - 1);
        return false;
    }
}
