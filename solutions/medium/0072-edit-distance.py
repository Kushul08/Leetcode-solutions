# ─────────────────────────────────────────────────
#  Problem : 0072. Edit Distance
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-08-26
# ─────────────────────────────────────────────────

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n,m=len(word1),len(word2)
        if n==0 and m==0:
            return 0
        elif n==0 and m!=0:
            return m
        elif n!=0 and m==0:
            return n
        def recur(i,j):
            if i<0 or j<0:
                return 0 if i<0 else i+1
            if word1[i]==word2[j]:
                return recur(i-1,j-1)
            else:
                return min(1+recur(i-1,j-1),
                            1+recur(i,j-1),
                            1+recur(i-1,j))
        return recur(n-1,m-1)
            