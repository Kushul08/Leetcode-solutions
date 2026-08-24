# ─────────────────────────────────────────────────
#  Problem : 1872. Stone Game VIII
#  Difficulty : Hard
#  Runtime  : 862 ms
#  Memory   : 24.9 MB
#  Solved   : 2026-08-24
# ─────────────────────────────────────────────────

class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n=len(stones)
        prefix=[stones[0]]
        for i in range(1,n):
            prefix.append(stones[i]+prefix[-1])
        dp=[0]*n
        dp[n-1]=prefix[n-1]
        for i in range(n-2,0,-1):
            dp[i]=max(dp[i+1],prefix[i]-dp[i+1])
        return dp[1]