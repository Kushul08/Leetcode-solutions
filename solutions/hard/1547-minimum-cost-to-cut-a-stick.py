# ─────────────────────────────────────────────────
#  Problem : 1547. Minimum Cost to Cut a Stick
#  Difficulty : Hard
#  Runtime  : 663 ms
#  Memory   : 34.6 MB
#  Solved   : 2026-08-30
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)
        cuts.sort()

        @lru_cache(None)
        def mcm(i,j):
            if i>j:
                return 0
            mini=1e9
            for k in range(i,j+1):
                steps=(cuts[j+1]-cuts[i-1])+mcm(i,k-1)+mcm(k+1,j)
                mini=min(mini,steps)
            return mini
        return mcm(1,len(cuts)-2)