# ─────────────────────────────────────────────────
#  Problem : 0115. Distinct Subsequences
#  Difficulty : Hard
#  Runtime  : 410 ms
#  Memory   : 43.7 MB
#  Solved   : 2026-08-25
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m=len(s),len(t)

        dp=[[-1]*(m) for _ in range(n)]
        def recur(i,j):
            if i<0 or j<0:
                return 1 if j==-1 else 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i]==t[j]:
                dp[i][j]=recur(i-1,j-1)+recur(i-1,j)
                return dp[i][j]
            else:
                dp[i][j]=recur(i-1,j)
                return dp[i][j]
        return recur(n-1,m-1)
