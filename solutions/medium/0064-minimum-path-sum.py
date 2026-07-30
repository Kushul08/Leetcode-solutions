# ─────────────────────────────────────────────────
#  Problem : 0064. Minimum Path Sum
#  Difficulty : Medium
#  Runtime  : 36 ms
#  Memory   : 32.9 MB
#  Solved   : 2026-07-30
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])

        @lru_cache(None)
        def recur(x,y):
            if x<0 or y<0:
                return float('inf')
            if x==0 and y==0:
                return grid[x][y]
            return min(recur(x-1,y),recur(x,y-1))+grid[x][y]
        return recur(m-1,n-1)
