# ─────────────────────────────────────────────────
#  Problem : 0583. Delete Operation for Two Strings
#  Difficulty : Medium
#  Runtime  : 133 ms
#  Memory   : 14.5 MB
#  Solved   : 2026-08-24
# ─────────────────────────────────────────────────

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n,m=len(word1),len(word2)

        dp=[[0]*m for _ in range(n)]
        dp[0][0]=1 if word1[0]==word2[0] else 0
        for i in range(1,m):
            if word2[i]==word1[0]:
                dp[0][i]=1
            else:
                dp[0][i]=dp[0][i-1]
        for i in range(1,n):
            if word1[i]==word2[0]:
                dp[i][0]=1
            else:
                dp[i][0]=dp[i-1][0]
        for i in range(1,n):
            for j in range(1,m):
                if word1[i]==word2[j]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return n+m-2*dp[n-1][m-1]