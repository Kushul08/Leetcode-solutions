# ─────────────────────────────────────────────────
#  Problem : 0120. Triangle
#  Difficulty : Medium
#  Runtime  : 33 ms
#  Memory   : 20.4 MB
#  Solved   : 2026-07-30
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        n=len(triangle)
        
        @lru_cache
        def recur(i,j):
            if i==n-1:
                return triangle[i][j]
            down=triangle[i][j]+recur(i+1,j)
            right=triangle[i][j]+recur(i+1,j+1)
            return min(down,right)
        return recur(0,0)