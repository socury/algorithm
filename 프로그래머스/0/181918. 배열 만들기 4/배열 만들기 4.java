class Solution {
    public int[] solution(int[] arr) {
        int[] stk = new int[arr.length];
        
        int top = -1;
        int i = 0;

        while (i < arr.length) {
            if (top == -1) 
                stk[++top] = arr[i++];
            else if (stk[top] < arr[i]) 
                stk[++top] = arr[i++];    
            else 
                top--;
        }

        int[] answer = new int[top + 1];
        
        for (int j = 0; j <= top; j++) 
            answer[j] = stk[j];
        return answer;
    }
}