# ─────────────────────────────────────────────────
#  Problem : 0583. Delete Operation for Two Strings
#  Difficulty : Medium
#  Runtime  : 112 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-08-24
# ─────────────────────────────────────────────────

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1)<len(word2):
            s1=word1
            s2=word2
        else:
            s1=word2
            s2=word1

        n,m=len(s1),len(s2)

        dp=[0]*n 
        dp[0]=1 if s1[0]==s2[0] else 0
        for i in range(1,n):
            if s1[i]==s2[0]:
                dp[i]=1
            else:
                dp[i]=dp[i-1]
                
        for i in range(1,m):
            temp=[0]*n
            if s1[0]==s2[i]: 
                temp[0]=1
            else:
                temp[0]=dp[0]
            for j in range(1,n):
                if s1[j]==s2[i]:
                    temp[j]=dp[j-1]+1
                else:
                    temp[j]=max(dp[j],temp[j-1])
            dp=temp
        return n+m-2*dp[n-1]