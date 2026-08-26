# ─────────────────────────────────────────────────
#  Problem : 0072. Edit Distance
#  Difficulty : Medium
#  Runtime  : 17 ms
#  Memory   : 25.1 MB
#  Solved   : 2026-08-26
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n,m=len(word1),len(word2)
        if n==0 and m==0:
            return 0
        elif n==0 and m!=0:
            return m
        elif n!=0 and m==0:
            return n
        
        @lru_cache(None)
        def recur(i,j):
            if i<0 or j<0:
                if i>=0:
                    return i+1
                if j>=0:
                    return j+1
                return 0
            if word1[i]==word2[j]:
                return recur(i-1,j-1)
            else:
                return min(1+recur(i-1,j-1),
                            1+recur(i,j-1),
                            1+recur(i-1,j))
        return recur(n-1,m-1)
            