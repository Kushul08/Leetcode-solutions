# ─────────────────────────────────────────────────
#  Problem : 0583. Delete Operation for Two Strings
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.3 MB
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
        def recur(i,j):
            if i<0 or j<0:
                return 0
            if word1[i]==word2[j]:
                return recur(i-1,j-1)+1
            else:
                return max(recur(i-1,j),
                            recur(i,j-1))
        lcs=recur(n-1,m-1)
        return n-lcs+m-lcs