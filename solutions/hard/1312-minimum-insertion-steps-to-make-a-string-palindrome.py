# ─────────────────────────────────────────────────
#  Problem : 1312. Minimum Insertion Steps to Make a String Palindrome
#  Difficulty : Hard
#  Runtime  : 795 ms
#  Memory   : 14.6 MB
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
        dp=[[0]*(n+1) for _ in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return n-dp[n][n]