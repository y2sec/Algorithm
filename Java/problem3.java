// 수식 최대화

import java.util.*;

class Solution {
    public long solution(String expression) {
        long answer = 0;
        int s = 0, e = 0;
        List<String> exprList = new ArrayList<>();
        for (int i = 0; i < expression.length(); i++) {
            char c = expression.charAt(i);
            if ('0' <= c && c <= '9') {
                e++;
            } else {
                exprList.add(expression.substring(s, e));
                exprList.add(expression.substring(e, e+1));
                s = ++e;
            }
        }
        exprList.add(expression.substring(s, e));

        answer = Math.max(answer, calculator(new ArrayList<>(exprList), new String[]{"*", "+", "-"}));
        answer = Math.max(answer, calculator(new ArrayList<>(exprList), new String[]{"*", "-", "+"}));
        answer = Math.max(answer, calculator(new ArrayList<>(exprList), new String[]{"+", "*", "-"}));
        answer = Math.max(answer, calculator(new ArrayList<>(exprList), new String[]{"+", "-", "*"}));
        answer = Math.max(answer, calculator(new ArrayList<>(exprList), new String[]{"-", "+", "*"}));
        answer = Math.max(answer, calculator(new ArrayList<>(exprList), new String[]{"-", "*", "+"}));

        return answer;
    }

    public long calculator(List<String> exprList, String[] operation) {
        for (String s : operation) {
            int j = 0;
            int leng = exprList.size();
            while (j < leng) {
                if (exprList.get(j).equals(s)) {
                    if (s.equals("+")) {
                        exprList.set(j - 1, String.valueOf(Long.parseLong(exprList.get(j - 1)) + Long.parseLong(exprList.get(j + 1))));
                    } else if (s.equals("-")) {
                        exprList.set(j - 1, String.valueOf(Long.parseLong(exprList.get(j - 1)) - Long.parseLong(exprList.get(j + 1))));
                    } else {
                        exprList.set(j - 1, String.valueOf(Long.parseLong(exprList.get(j - 1)) * Long.parseLong(exprList.get(j + 1))));
                    }
                    exprList.remove(j + 1);
                    exprList.remove(j);
                    leng -= 2;
                } else {
                    j++;
                }

            }
        }
        return Math.abs(Long.parseLong(exprList.get(0)));
    }
}