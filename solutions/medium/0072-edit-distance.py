# ─────────────────────────────────────────────────
#  Problem : 0072. Edit Distance
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.3 MB
#  Solved   : 2026-08-26
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n,m=len(word1),len(word2)
        if n==0 and m==0:
            return 0
        elif n==0 and m!=0:
            return m
        elif n!=0 and m==0:
            return n
        
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            dp[i][0]=i+1

        for j in range(m):
            dp[0][j]=j+1
        dp[0][0]=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(1+dp[i-1][j-1],
                                1+dp[i][j-1],
                                1+dp[i-1][j])
        print(dp)     
        return dp[n][m]
            