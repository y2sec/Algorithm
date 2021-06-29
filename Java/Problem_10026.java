// 10026 적록색약

package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Problem_10026 {

    static int[] dx = new int[]{1, -1, 0, 0};
    static int[] dy = new int[]{0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        char draw[][] = new char[n][n];

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < n; j++) {
                draw[i][j] = line.charAt(j);
            }
        }

        boolean[][] visited = new boolean[n][n];

        int standardResult = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j]) {
                    continue;
                }
                bfs(visited, draw, Collections.singletonList(draw[i][j]), i, j);
                standardResult++;
            }
        }

        visited = new boolean[n][n];

        int blindResult = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j]) {
                    continue;
                }

                if (draw[i][j] == 'R' || draw[i][j] == 'G') {
                    bfs(visited, draw, Arrays.asList('R', 'G'), i, j);
                } else {
                    bfs(visited, draw, Collections.singletonList('B'), i, j);
                }

                blindResult++;
            }
        }

        System.out.println(standardResult + " " + blindResult);
    }

    static void bfs(boolean[][] visited, char[][] draw, List<Character> colors, int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x, y});

        visited[x][y] = true;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();

            for (int i = 0; i < 4; i++) {
                int nX = current[0] + dx[i];
                int nY = current[1] + dy[i];

                if (nX < 0 || nY < 0 || nX >= draw.length || nY >= draw.length) {
                    continue;
                }

                if (!colors.contains(draw[nX][nY])) {
                    continue;
                }

                if (visited[nX][nY]) {
                    continue;
                }

                visited[nX][nY] = true;
                queue.add(new int[]{nX, nY});
            }
        }
    }
}
