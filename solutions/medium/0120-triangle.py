# ─────────────────────────────────────────────────
#  Problem : 0120. Triangle
#  Difficulty : Medium
#  Runtime  : 6 ms
#  Memory   : 13 MB
#  Solved   : 2026-07-30
# ─────────────────────────────────────────────────

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n=len(triangle)
        dp=[triangle[0][0]]
        for i in range(1,n):
            temp=[0]*len(triangle[i])
            for j in range(len(triangle[i])):
                left=dp[j-1] if 0<=j-1 else 1e9
                up=dp[j] if j<len(triangle[i-1]) else 1e9
                temp[j]=min(left,up)+triangle[i][j]
            dp=temp
        return min(dp)