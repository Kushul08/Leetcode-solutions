# ─────────────────────────────────────────────────
#  Problem : 1277. Count Square Submatrices with All Ones
#  Difficulty : Medium
#  Runtime  : 71 ms
#  Memory   : 13.5 MB
#  Solved   : 2026-08-31
# ─────────────────────────────────────────────────

class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n,m=len(matrix),len(matrix[0])
        dp=[[0]*m for _ in range(n)]
        for i in range(m):
            dp[0][i]=matrix[0][i]
        for j in range(n):
            dp[j][0]=matrix[j][0]
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j]==0: continue
                dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        ans=0
        for row in dp:
            ans+=sum(row)
        return ans