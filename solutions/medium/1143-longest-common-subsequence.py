# ─────────────────────────────────────────────────
#  Problem : 1143. Longest Common Subsequence
#  Difficulty : Medium
#  Runtime  : 409 ms
#  Memory   : 12.4 MB
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
        dp=[0]*n 
        if text1[0]==text2[0]: dp[0]=1
        for i in range(1,n):
            if text2[0]==text1[i]:
                dp[i]=1
            elif i>0: 
                dp[i]=dp[i-1]
       

        for i in range(1,m):
            temp=[0]*n
            temp[0]= 1 if text2[i]==text1[0] else dp[0]
            for j in range(1,n):
                if text2[i]==text1[j]:
                    temp[j]=dp[j-1]+1
                else:
                    temp[j]=max(temp[j-1],dp[j])
            dp=temp
        return dp[n-1]