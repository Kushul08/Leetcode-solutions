# ─────────────────────────────────────────────────
#  Problem : 1547. Minimum Cost to Cut a Stick
#  Difficulty : Hard
#  Runtime  : 0 ms
#  Memory   : 19.4 MB
#  Solved   : 2026-08-30
# ─────────────────────────────────────────────────

class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        cuts.append(0)
        cuts.append(n)
        cuts.sort()

        def mcm(i,j):
            if i>j:
                return 0
            mini=1e9
            for k in range(i,j+1):
                steps=(cuts[j+1]-cuts[i-1])+mcm(i,k-1)+mcm(k+1,j)
                mini=min(mini,steps)
            return mini
        return mcm(1,len(cuts)-2)