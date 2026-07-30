# ─────────────────────────────────────────────────
#  Problem : 0064. Minimum Path Sum
#  Difficulty : Medium
#  Runtime  : 11 ms
#  Memory   : 14.1 MB
#  Solved   : 2026-07-30
# ─────────────────────────────────────────────────

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n=len(grid),len(grid[0])
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=grid[0][0]
        for i in range(1,n):
            dp[0][i]=dp[0][i-1]+grid[0][i]
        for i in range(1,m):
            dp[i][0]=dp[i-1][0]+grid[i][0]
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]