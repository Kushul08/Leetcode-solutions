# ─────────────────────────────────────────────────
#  Problem : 0062. Unique Paths
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-07-29
# ─────────────────────────────────────────────────

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp=[1]*n
        for x in range(1,m):
            col=1
            for y in range(1,n):
                dp[y]=col+dp[y]
                col=dp[y]
        return dp[n-1]
