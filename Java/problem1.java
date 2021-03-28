// 단체사진 찍기

import java.util.ArrayList;
import java.util.List;

public class problem1 {

    List<String> combinations = new ArrayList<>();
    String[] friends = {"A", "C", "F", "J", "M", "N", "R", "T"};

    public static void main(String[] args) {
        problem1 problem1 = new problem1();
        String[] data = {"N~F=0", "R~T>2"};
        System.out.println(problem1.solution(2, data));
    }

    public int solution(int n, String[] data) {
        int answer = 0;

        combinations(friends, "");
        List<Integer> isAvailable = new ArrayList<>();

        for (int i = 0; i < combinations.size(); i++)
            isAvailable.add(1);

        for (String condition : data) {
            String friendA = String.valueOf(condition.charAt(0));
            String friendB = String.valueOf(condition.charAt(2));
            String sign = String.valueOf(condition.charAt(3));
            int num = Integer.parseInt(String.valueOf(condition.charAt(4)));

            for (int i = 0; i < combinations.size(); i++) {
                if (isAvailable.get(i) == 0)
                    continue;

                int diff_friends = Math.abs(combinations.get(i).indexOf(friendA) - combinations.get(i).indexOf(friendB));
                switch (sign) {
                    case "=":
                        if (diff_friends != num+1)
                            isAvailable.set(i, 0);
                        break;
                    case "<":
                        if (diff_friends >= num+1)
                            isAvailable.set(i, 0);
                        break;
                    case ">":
                        if (diff_friends <= num+1)
                            isAvailable.set(i, 0);
                        break;
                }
            }
        }

        for (Integer nn : isAvailable) {
            if (nn == 1)
                answer++;
        }

        return answer;
    }

    public void combinations(String[] friends, String combination) {
        if (combination.length() == friends.length) {
            combinations.add(combination);
            return;
        }
        for (String friend : friends) {
            if (!combination.contains(friend)) {
                combinations(friends, combination + friend);
            }
        }
    }
}
