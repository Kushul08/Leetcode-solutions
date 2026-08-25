# ─────────────────────────────────────────────────
#  Problem : 0115. Distinct Subsequences
#  Difficulty : Hard
#  Runtime  : 675 ms
#  Memory   : 218.5 MB
#  Solved   : 2026-08-25
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m=len(s),len(t)

        @lru_cache(None)
        def recur(i,j):
            if i<0 or j<0:
                return 1 if j==-1 else 0
            if s[i]==t[j]:
                return recur(i-1,j-1)+recur(i-1,j)
            else:
                return recur(i-1,j)
        return recur(n-1,m-1)
