# ─────────────────────────────────────────────────
#  Problem : 1312. Minimum Insertion Steps to Make a String Palindrome
#  Difficulty : Hard
#  Runtime  : 1274 ms
#  Memory   : 27 MB
#  Solved   : 2026-08-19
# ─────────────────────────────────────────────────

class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1=s
        s2=s[::-1]

        n=len(s)
        dp=[[-1]*n for _ in range(n)]
        def recur(i,j):
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if s1[i]==s2[j]:
                dp[i][j]=recur(i-1,j-1)+1
                return dp[i][j]
            else:
                dp[i][j]=max(recur(i,j-1),recur(i-1,j))
                return dp[i][j]

        return n-recur(n-1,n-1)