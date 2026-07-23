# ─────────────────────────────────────────────────
#  Problem : 0070. Climbing Stairs
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 19.2 MB
#  Solved   : 2026-07-23
# ─────────────────────────────────────────────────

class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*46
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]