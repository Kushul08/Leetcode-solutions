# ─────────────────────────────────────────────────
#  Problem : 0064. Minimum Path Sum
#  Difficulty : Medium
#  Runtime  : 15 ms
#  Memory   : 13.8 MB
#  Solved   : 2026-07-30
# ─────────────────────────────────────────────────

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n=len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if i==0:
                    if j!=0:  
                        grid[i][j]+=grid[i][j-1]
                elif j==0:
                    grid[i][j]+=grid[i-1][j]
                else:
                    grid[i][j]=min(grid[i-1][j],grid[i][j-1]) + grid[i][j]
        return grid[m-1][n-1]