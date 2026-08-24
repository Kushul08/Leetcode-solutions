# ─────────────────────────────────────────────────
#  Problem : 0583. Delete Operation for Two Strings
#  Difficulty : Medium
#  Runtime  : 164 ms
#  Memory   : 15.4 MB
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

        dp=[[-1]*m for _ in range(n)]

        def recur(i,j):
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if word1[i]==word2[j]:
                dp[i][j]=recur(i-1,j-1)+1
                return dp[i][j]
            else:
                dp[i][j]=max(recur(i-1,j),
                            recur(i,j-1))
                return dp[i][j]
        lcs=recur(n-1,m-1)
        return n-lcs+m-lcs