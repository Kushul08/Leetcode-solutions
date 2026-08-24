# ─────────────────────────────────────────────────
#  Problem : 0583. Delete Operation for Two Strings
#  Difficulty : Medium
#  Runtime  : 143 ms
#  Memory   : 61 MB
#  Solved   : 2026-08-24
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n,m=len(word1),len(word2)

        @lru_cache(None)
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