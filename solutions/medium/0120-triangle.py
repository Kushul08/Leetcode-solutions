# ─────────────────────────────────────────────────
#  Problem : 0120. Triangle
#  Difficulty : Medium
#  Runtime  : 8 ms
#  Memory   : 13.2 MB
#  Solved   : 2026-07-30
# ─────────────────────────────────────────────────

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n=len(triangle)
        for i in range(1,n):
            for j in range(len(triangle[i])):
                left=triangle[i-1][j-1] if 0<=j-1 else 1e9
                up=triangle[i-1][j] if j<len(triangle[i-1]) else 1e9
                triangle[i][j]=min(left,up)+triangle[i][j]
        return min(triangle[n-1])