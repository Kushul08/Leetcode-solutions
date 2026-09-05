# ─────────────────────────────────────────────────
#  Problem : 1277. Count Square Submatrices with All Ones
#  Difficulty : Medium
#  Runtime  : 70 ms
#  Memory   : 13.6 MB
#  Solved   : 2026-09-05
# ─────────────────────────────────────────────────

class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n,m=len(matrix),len(matrix[0])
        dp=[[0]*m for _ in range(n)]
        ans=0
        for i in range(n):
            dp[i][0]=matrix[i][0]
            ans+=dp[i][0]
        for j in range(m):
            dp[0][j]=matrix[0][j]
            ans+=dp[0][j]
        ans-=matrix[0][0]#here the origin is counted twice so i deleted it for once
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j]==0: 
                    continue
                dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                ans+=dp[i][j]
        
        return ans