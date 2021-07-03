// 1072 게임

package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Problem_1072 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long X = Integer.parseInt(st.nextToken());
        long Y = Integer.parseInt(st.nextToken());
        long Z = (Y * 100) / X;

        if (Z >= 99) {
            System.out.println(-1);
        } else {
            long min = 1;
            long max = 1000000000;
            long mid = (min + max) / 2;

            long result = 1000000000;
            while (min <= max) {
                long resultZ = ((Y + mid) * 100) / (X + mid);

                if (resultZ > Z) {
                    result = Math.min(result, mid);
                    max = mid - 1;
                } else {
                    min = mid + 1;
                }
                mid = (min + max) / 2;
            }
            System.out.println(result);
        }


    }

}
