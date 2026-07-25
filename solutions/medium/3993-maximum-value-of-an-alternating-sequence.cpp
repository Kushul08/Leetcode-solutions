// ─────────────────────────────────────────────────
//  Problem : 3993. Maximum Value of an Alternating Sequence
//  Difficulty : Medium
//  Runtime  : 0 ms
//  Memory   : 7.9 MB
//  Solved   : 2026-07-25
// ─────────────────────────────────────────────────

class Solution {
public:
    long long maximumValue(int n, int s, int m) {
        int m_count=n/2;
        int one_count=(n-1)/2;
        if (n%2==0){ return static_cast<long>(s)+static_cast<long>(m)*m_count-one_count;}
        return static_cast<long>(s)+static_cast<long>(m)*m_count-one_count+1;
    }
};