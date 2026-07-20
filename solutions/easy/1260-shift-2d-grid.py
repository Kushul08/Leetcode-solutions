# ─────────────────────────────────────────────────
#  Problem : 1260. Shift 2D Grid
#  Difficulty : Easy
#  Runtime  : 597 ms
#  Memory   : 12.7 MB
#  Solved   : 2026-07-20
# ─────────────────────────────────────────────────

class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m=len(grid)
        n=len(grid[0])
        ans=[g[:] for g in grid]

        for _ in range(k):
            for i in range(m):
                for j in range(n):
                    if j+1<n:
                        ans[i][j+1]=grid[i][j]
                    if i+1<m:
                        ans[i+1][0]=grid[i][n-1]
                    ans[0][0]=grid[m-1][n-1]
            grid = [row[:] for row in ans]
        # print(grid,ans)
        return ans