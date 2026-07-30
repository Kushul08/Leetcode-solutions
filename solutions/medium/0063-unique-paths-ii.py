# ─────────────────────────────────────────────────
#  Problem : 0063. Unique Paths II
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.2 MB
#  Solved   : 2026-07-30
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
        dp=[0]*m 
        for i in range(m):
            if obstacleGrid[0][i]==1:
                break
            dp[i]=1
        row=0
        for i in range(n):
            if obstacleGrid[i][0]==1:
                row=i
                break
        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j]==1: continue
                up=dp[j] if obstacleGrid[i-1][j]==0 else 0
                left=dp[j-1] if obstacleGrid[i][j-1]==0 else 0
                dp[j]=up+left
                left=dp[j]
        return dp[m-1]