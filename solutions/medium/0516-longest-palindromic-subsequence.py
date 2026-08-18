# ─────────────────────────────────────────────────
#  Problem : 0516. Longest Palindromic Subsequence
#  Difficulty : Medium
#  Runtime  : 38 ms
#  Memory   : 14 MB
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
        dp=[[-1]*n for _ in range(n)]
        dp[0][0]=1 if s1[0]==s2[0] else 0
        for i in range(1,n):
            if s1[0]==s2[i]:
                dp[0][i]=1
            else:
                dp[0][i]=dp[0][i-1]
        for i in range(1,n):
            if s1[i]==s2[i]:
                dp[i][0]=1
            else:
                dp[i][0]=dp[i-1][0]
        for i in range(1,n):
            for j in range(1,n):
                if s1[i]==s2[j]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        return dp[n-1][n-1]