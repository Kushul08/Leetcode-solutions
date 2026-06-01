# ─────────────────────────────────────────────────
#  Problem : 2144. Minimum Cost of Buying Candies With Discount
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.3 MB
#  Solved   : 2026-06-01
# ─────────────────────────────────────────────────

class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort()
        i=len(cost)-1
        ans=0
        while i>-1:
            if i>=0 and i-1>=0:
                ans+=cost[i]+cost[i-1]
                i-=3
            else:
                ans+=cost[i]
                i-=1
        return ans
            