# ─────────────────────────────────────────────────
#  Problem : 0115. Distinct Subsequences
#  Difficulty : Hard
#  Runtime  : 416 ms
#  Memory   : 75.7 MB
#  Solved   : 2026-08-25
# ─────────────────────────────────────────────────

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m=len(s),len(t)

        dp=[[0]*(m+1) for _ in range(n+1)]
        dp[0][0]=1 if s[0]==t[0] else 0
        for j in range(n):
            dp[j][0]=1
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][m]
