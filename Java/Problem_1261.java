// 1261 알고스팟

package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Problem_1261 {

    static int[] dx = new int[]{1, 0, -1, 0};
    static int[] dy = new int[]{0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] size = br.readLine().split(" ");
        int N = Integer.parseInt(size[0]);
        int M = Integer.parseInt(size[1]);

        char[][] maze = new char[M][N];

        for (int i = 0; i < M; i++) {
            String s = br.readLine();
            for (int j = 0; j < N; j++) {
                maze[i][j] = s.charAt(j);
            }
        }

        int[][] wall = new int[M][N];
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                wall[i][j] = N * M;
            }
        }

        wall[0][0] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o[0]));

        pq.add(new int[]{0, 0, 0});

        while (!pq.isEmpty()) {
            int[] current = pq.poll();

            if (current[0] > wall[current[1]][current[2]]) {
                continue;
            }

            for (int i = 0; i < 4; i++) {
                int[] next = new int[]{current[0] , current[1] + dx[i], current[2] + dy[i]};

                if (next[1] < 0 || next[2] < 0 || next[1] >= M || next[2] >= N) {
                    continue;
                }

                if (maze[next[1]][next[2]] == '1') {
                    next[0] += 1;
                }

                if (wall[next[1]][next[2]] <= next[0]) {
                    continue;
                }

                wall[next[1]][next[2]] = next[0];
                pq.add(next);
            }
        }

        System.out.println(wall[M-1][N-1]);
    }

}
