# ─────────────────────────────────────────────────
#  Problem : 0063. Unique Paths II
#  Difficulty : Medium
#  Runtime  : 2 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-07-29
# ─────────────────────────────────────────────────

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n,m=len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[0][0]==1 or obstacleGrid[n-1][m-1]==1:
            return 0
        dp=[[0]*m for _ in range(n)]
        for i in range(m):
            if obstacleGrid[0][i]==1:
                break
            dp[0][i]=1
        for i in range(n):
            if obstacleGrid[i][0]==1:
                break
            dp[i][0]=1
        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j]==1: continue
                up=dp[i-1][j] if obstacleGrid[i-1][j]==0 else 0
                left=dp[i][j-1] if obstacleGrid[i][j-1]==0 else 0
                dp[i][j]=up+left
        return dp[n-1][m-1] 