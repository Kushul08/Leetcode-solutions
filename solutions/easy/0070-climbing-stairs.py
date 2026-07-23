# ─────────────────────────────────────────────────
#  Problem : 0070. Climbing Stairs
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 19.2 MB
#  Solved   : 2026-07-23
# ─────────────────────────────────────────────────

class Solution:
    dp=[0]*46
    def climbStairs(self, n: int) -> int:
        self.dp[1]=1
        self.dp[2]=2
        for i in range(3,n+1):
            self.dp[i]=self.dp[i-1]+self.dp[i-2]
        return self.dp[n]