import java.util.*;

class Solution {
    public int solution(int a, int b, int c, int d) {
        int[] cnt = new int[7];
        cnt[a]++; cnt[b]++; cnt[c]++; cnt[d]++;

        List<Integer> one = new ArrayList<>();
        List<Integer> two = new ArrayList<>();
        int three = 0, four = 0;

        for (int i = 1; i <= 6; i++) {
            if (cnt[i] == 4) four = i;
            if (cnt[i] == 3) three = i;
            if (cnt[i] == 2) two.add(i);
            if (cnt[i] == 1) one.add(i);
        }

        if (four != 0) return 1111 * four;
        if (three != 0 && one.size() == 1) return (int)Math.pow(10 * three + one.get(0), 2);
        if (two.size() == 2) return (two.get(0) + two.get(1)) * Math.abs(two.get(0) - two.get(1));
        if (two.size() == 1 && one.size() == 2) return one.get(0) * one.get(1);
        return Math.min(Math.min(a, b), Math.min(c, d));
    }
}