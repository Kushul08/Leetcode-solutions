# ─────────────────────────────────────────────────
#  Problem : 0132. Palindrome Partitioning II
#  Difficulty : Hard
#  Runtime  : 2780 ms
#  Memory   : 19.2 MB
#  Solved   : 2026-08-31
# ─────────────────────────────────────────────────

class Solution:
    def minCut(self, s: str) -> int:
        
        if s==s[::-1]:
            return 0
        n=len(s)
        dp=[-1]*(n+1)
        for i in range(n-1,-1,-1):
            mini=1e9
            for k in range(i,n):
                if (i==0 and s[:k+1]==s[k::-1]) or s[i:k+1]==s[k:i-1:-1] :
                    steps=1+dp[k+1]
                    mini=min(mini,steps)
            dp[i]=mini
        return dp[0]