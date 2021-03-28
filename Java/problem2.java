// 행렬의 곱셉

public class problem2 {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int arr_col = arr1.length;
        int arr_row = arr2[0].length;
        int[][] answer = new int[arr_col][arr_row];

        for (int col = 0; col < arr_col; col++) {
            for (int row = 0; row < arr_row; row++) {
                for (int idx = 0; idx < arr1[0].length; idx++) {
                    answer[col][row] += arr1[col][idx] * arr2[idx][row];
                }
            }
        }

        return answer;
    }
}
