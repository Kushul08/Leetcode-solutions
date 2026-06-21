# ─────────────────────────────────────────────────
#  Problem : 1833. Maximum Ice Cream Bars
#  Difficulty : Medium
#  Runtime  : 144 ms
#  Memory   : 21 MB
#  Solved   : 2026-06-21
# ─────────────────────────────────────────────────

class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        max_ice=0
        for i in range(len(costs)):
            if costs[i]>coins:
                break
            if coins==0: break
            max_ice+=1
            coins-=costs[i]
        return max_ice