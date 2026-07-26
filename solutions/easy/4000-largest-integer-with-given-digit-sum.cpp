// ─────────────────────────────────────────────────
//  Problem : 4000. Largest Integer With Given Digit Sum
//  Difficulty : Easy
//  Runtime  : 0 ms
//  Memory   : 8.1 MB
//  Solved   : 2026-07-26
// ─────────────────────────────────────────────────

class Solution {
public:
    int largestInteger(int n, int s) {
        if (s==0){ return 0;}

        int sums=0;
        int num=0;
        for (int i=0; i<n;i++){
            for (int j=9; j>=0;j--){
                if (sums+j<=s){
                    num=num*10+j;
                    sums+=j;
                    break;
                }
                
            }
        }
        if (sums==s){
            return num;
        }
        return -1;
    }
};