class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int sum = 0;
        for (int n : num_list)
            sum += n;
        
        int mul = 1;
        for (int n : num_list)
            mul *= n;
        
        if (mul < (sum*sum))
            answer = 1;
        else if (mul > (sum*sum))
            answer = 0;
        
        return answer;
    }
}