# ─────────────────────────────────────────────────
#  Problem : 1312. Minimum Insertion Steps to Make a String Palindrome
#  Difficulty : Hard
#  Runtime  : 706 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-08-20
# ─────────────────────────────────────────────────

class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int`
        """
        s1=s
        s2=s[::-1]

        n=len(s)
        dp=[0]*(n+1)
        
        for i in range(1,n+1):
            temp=[0]*(n+1)
            for j in range(1,n+1):
                if s1[i-1]==s2[j-1]:
                    temp[j]=dp[j-1]+1
                else:
                    temp[j]=max(dp[j],temp[j-1])
            dp=temp
        return n-dp[n]