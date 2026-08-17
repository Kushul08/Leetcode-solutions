# ─────────────────────────────────────────────────
#  Problem : 1143. Longest Common Subsequence
#  Difficulty : Medium
#  Runtime  : 1054 ms
#  Memory   : 318.6 MB
#  Solved   : 2026-08-17
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n,m=len(text1),len(text2)

        @lru_cache(None)
        def recur(i,j):
            if i<0 or j<0: return 0
            if text1[i]==text2[j]:
                return recur(i-1,j-1)+1
            else:
                return max(recur(i-1,j),recur(i,j-1))
        return recur(n-1,m-1)
