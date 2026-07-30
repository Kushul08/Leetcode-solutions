# ─────────────────────────────────────────────────
#  Problem : 0064. Minimum Path Sum
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.5 MB
#  Solved   : 2026-07-30
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])

        @lru_cache
        def recur(x,y):
            if x<0 or y<0:
                return 201
            if x==0 and y==0:
                return grid[x][y]
            up=recur(x-1,y)+grid[x][y]
            left=recur(x,y-1)+grid[x][y]
            return min(up,left)
        return recur(m-1,n-1)
