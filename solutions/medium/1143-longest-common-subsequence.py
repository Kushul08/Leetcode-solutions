# ─────────────────────────────────────────────────
#  Problem : 1143. Longest Common Subsequence
#  Difficulty : Medium
#  Runtime  : 2 ms
#  Memory   : 12.3 MB
#  Solved   : 2026-08-17
# ─────────────────────────────────────────────────

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n,m=len(text1),len(text2)
        dp=[[0]*n for _ in range(m)]
        if text1[0]==text2[0]: dp[0][0]=1
        for i in range(1,n):
            if text2[0]==text1[i]:
                dp[0][i]=dp[0][i-1]+1
            else: dp[0][i]=dp[0][i-1]
        for j in range(m):
            if text1[0]==text2[j]:
                dp[j][0]=dp[j-1][0]+1
            else: 
                dp[j][0]=dp[j-1][0]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                if text2[i]==text1[j]:
                    dp[i][j]+=1
        
        return dp[m-1][n-1]