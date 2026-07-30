# ─────────────────────────────────────────────────
#  Problem : 0120. Triangle
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.4 MB
#  Solved   : 2026-07-30
# ─────────────────────────────────────────────────

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n=len(triangle)

        def recur(i,j):
            if i==n-1:
                return triangle[i][j]
            down=triangle[i][j]+recur(i+1,j)
            right=triangle[i][j]+recur(i+1,j+1)
            return min(down,right)
        return recur(0,0)