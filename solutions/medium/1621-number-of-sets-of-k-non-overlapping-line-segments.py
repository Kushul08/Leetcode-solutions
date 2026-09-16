# ─────────────────────────────────────────────────
#  Problem : 1621. Number of Sets of K Non-Overlapping Line Segments
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.5 MB
#  Solved   : 2026-09-16
# ─────────────────────────────────────────────────

from math import comb
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD=int(1e9+7)

        return comb(n+k-1,k*2)%MOD