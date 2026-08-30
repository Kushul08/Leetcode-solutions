# ─────────────────────────────────────────────────
#  Problem : 1547. Minimum Cost to Cut a Stick
#  Difficulty : Hard
#  Runtime  : 583 ms
#  Memory   : 12.5 MB
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
        dp=[[0]*(len(cuts)) for _ in range(len(cuts))]

        for i in range(len(cuts)-2,-1,-1):
            for j in range(i,len(cuts)-1):
                mini=1e9
                for k in range(i,j+1):
                    steps=(cuts[j+1]-cuts[i-1])+dp[i][k-1]+dp[k+1][j]
                    mini=min(mini,steps)
                dp[i][j]=mini
        return dp[1][len(cuts)-2]