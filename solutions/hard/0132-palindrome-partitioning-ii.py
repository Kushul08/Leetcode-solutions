# ─────────────────────────────────────────────────
#  Problem : 0132. Palindrome Partitioning II
#  Difficulty : Hard
#  Runtime  : 3045 ms
#  Memory   : 20 MB
#  Solved   : 2026-08-31
# ─────────────────────────────────────────────────

class Solution:
    def minCut(self, s: str) -> int:
        
        if s==s[::-1]:
            return 0
        n=len(s)
        dp=[-1]*n
        def recur(i):
            if i==n:
                return -1
            if dp[i]!=-1:
                return dp[i]
            mini=1e9
            for k in range(i,n):
                if (i==0 and s[:k+1]==s[k::-1]) or s[i:k+1]==s[k:i-1:-1] :
                    steps=1+recur(k+1)
                    mini=min(mini,steps)
            dp[i]=mini
            return dp[i]
        return recur(0)