# ─────────────────────────────────────────────────
#  Problem : 0115. Distinct Subsequences
#  Difficulty : Hard
#  Runtime  : 686 ms
#  Memory   : 240.8 MB
#  Solved   : 2026-08-25
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m=len(s),len(t)

        @lru_cache(None)
        def recur(i,j,match):
            if i<0 or j<0:
                if match==m:
                    return 1
                return 0
            if s[i]==t[j]:
                return recur(i-1,j-1,match+1)+recur(i-1,j,match)
            else:
                return recur(i-1,j,match)
        return recur(n-1,m-1,0)
