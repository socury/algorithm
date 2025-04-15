class Solution {
    public String solution(String code) {
        StringBuilder ret = new StringBuilder();
        int mode = 0;

        for (int i = 0; i < code.length(); i++) {
            char ch = code.charAt(i);
            if (ch == '1') {
                mode = 1 - mode; // mode 토글
            } else {
                if (mode == 0 && i % 2 == 0) {
                    ret.append(ch);
                } else if (mode == 1 && i % 2 == 1) {
                    ret.append(ch);
                }
            }
        }
        
        if (ret.toString().length() == 0)
            return "EMPTY";
        else
            return ret.toString();
    }
}