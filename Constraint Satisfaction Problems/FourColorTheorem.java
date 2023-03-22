public class FourColorTheorem {
    private static final int MAX_COLORS = 4;

    public static void main(String[] args) {
        int[][] graph = {
                { 0, 1, 1, 1, 0, 0, 0 },
                { 1, 0, 1, 0, 1, 0, 0 },
                { 1, 1, 0, 1, 1, 0, 0 },
                { 1, 0, 1, 0, 1, 1, 1 },
                { 0, 1, 1, 1, 0, 1, 0 },
                { 0, 0, 0, 1, 1, 0, 1 },
                { 0, 0, 0, 1, 0, 1, 0 }
        }; // Adjacency matrix of the graph to be colored

        int[] colors = new int[graph.length]; // Array to store colors of vertices

        if (colorGraph(graph, colors, 0)) {
            System.out.println("The graph can be colored with 4 colors.");
            System.out.print("The vertex colors are: ");
            for (int i = 0; i < colors.length; i++) {
                System.out.print(colors[i] + " ");
            }
        } else {
            System.out.println("The graph cannot be colored with 4 colors.");
        }
    }

    public static boolean colorGraph(int[][] graph, int[] colors, int vertex) {
        if (vertex == graph.length) { // All vertices have been colored
            return true;
        }

        for (int color = 1; color <= MAX_COLORS; color++) {
            if (isColorValid(graph, colors, vertex, color)) {
                colors[vertex] = color; // Assign the color to the vertex

                if (colorGraph(graph, colors, vertex + 1)) { // Recursively color the next vertex
                    return true;
                }

                colors[vertex] = 0; // Backtrack and try a different color
            }
        }

        return false; // No valid color found
    }

    public static boolean isColorValid(int[][] graph, int[] colors, int vertex, int color) {
        for (int i = 0; i < graph.length; i++) {
            if (graph[vertex][i] == 1 && colors[i] == color) { // Check if adjacent vertices have the same color
                return false;
            }
        }

        return true; // Color is valid
    }
}
