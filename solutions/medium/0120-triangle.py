# ─────────────────────────────────────────────────
#  Problem : 0120. Triangle
#  Difficulty : Medium
#  Runtime  : 4 ms
#  Memory   : 13.4 MB
#  Solved   : 2026-07-30
# ─────────────────────────────────────────────────

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n=len(triangle)
        dp=[[0]*i for i in range(1,n+1)]
        dp[0][0]=triangle[0][0]

        for i in range(1,n):
            for j in range(len(triangle[i])):
                left=dp[i-1][j-1] if 0<=j-1 else 1e9
                up=dp[i-1][j] if j<len(triangle[i-1]) else 1e9
                dp[i][j]=min(left,up)+triangle[i][j]
        return min(dp[n-1])