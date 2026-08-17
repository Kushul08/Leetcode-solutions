# ─────────────────────────────────────────────────
#  Problem : 1143. Longest Common Subsequence
#  Difficulty : Medium
#  Runtime  : 415 ms
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
        s1=''
        s2=''
        if n<m:
            s1=text1
            s2=text2
        else:
            s1=text2
            s2=text1
        
        dp=[0]*len(s1)
        dp[0]= 1 if s1[0]==s2[0] else 0
        for i in range(1,len(s1)):
            if s1[i]==s2[0]:
                dp[i]=1
            else:
                dp[i]=dp[i-1]
        
        for i in range(1,len(s2)):
            temp=[0]*len(s1)
            temp[0]= 1 if s1[0]==s2[i] else dp[0]
            for j in range(1,len(s1)):
                if s2[i]==s1[j]:
                    temp[j]=dp[j-1]+1
                else:
                    temp[j]=max(temp[j-1],dp[j])
            dp=temp
        return dp[len(s1)-1]