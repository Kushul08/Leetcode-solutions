# ─────────────────────────────────────────────────
#  Problem : 0120. Triangle
#  Difficulty : Medium
#  Runtime  : 7 ms
#  Memory   : 13.5 MB
#  Solved   : 2026-07-30
# ─────────────────────────────────────────────────

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n=len(triangle)
        dp=[[0]*i for i in range(1,n+1)]
        # print(dp)
        dp[0][0]=triangle[0][0]

        for i in range(1,n):
            for j in range(len(triangle[i])):
                if 0<=j-1:
                    left=dp[i-1][j-1]
                else:
                    left=1e9
                if j<len(triangle[i-1]):
                    up=dp[i-1][j]
                else:
                    up=1e9
                dp[i][j]=min(left,up)+triangle[i][j]
        # print(dp)
        return min(dp[n-1])