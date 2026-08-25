# ─────────────────────────────────────────────────
#  Problem : 0115. Distinct Subsequences
#  Difficulty : Hard
#  Runtime  : 254 ms
#  Memory   : 19.6 MB
#  Solved   : 2026-08-25
# ─────────────────────────────────────────────────

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m=len(s),len(t)

        dp=[0]*(m+1)
        dp[0]=1 
        for i in range(1,n+1):
            temp=[0]*(m+1)
            temp[0]=1
            for j in range(1,m+1):
                if s[i-1]==t[j-1]:
                    temp[j]=dp[j-1]+dp[j]
                else:
                    temp[j]=dp[j]
            dp=temp
        return dp[m]
