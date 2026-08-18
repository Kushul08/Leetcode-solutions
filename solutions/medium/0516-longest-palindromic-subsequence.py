# ─────────────────────────────────────────────────
#  Problem : 0516. Longest Palindromic Subsequence
#  Difficulty : Medium
#  Runtime  : 1271 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-08-18
# ─────────────────────────────────────────────────

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        s1=s
        s2=s[::-1]
        dp=[0]*n 
        dp[0]=1 if s1[0]==s2[0] else 0
        for i in range(1,n):
            if s1[0]==s2[i]:
                dp[i]=1
            else:
                dp[i]=dp[i-1]
        for i in range(1,n):
            temp=[0]*n
            temp[0]= 1 if s1[i]==s2[0] else dp[0]
            for j in range(1,n):
                if s1[i]==s2[j]:
                    temp[j]=dp[j-1]+1
                else:
                    temp[j]=max(temp[j-1],dp[j])
            dp=temp
        return dp[n-1]