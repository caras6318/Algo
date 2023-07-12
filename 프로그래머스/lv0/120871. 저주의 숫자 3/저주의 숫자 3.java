
class Solution {
    public int solution(int n) {
        int answer = 0;
        int cnt = 0;
        
        
        for(int i=1; i <= n+cnt; i++){
            if(i % 3 == 0 || i % 10 == 3 || i / 10 == 3 || i / 10 == 13){
                cnt++;
            }
        }
        answer = n + cnt;
        return answer;
    }
}