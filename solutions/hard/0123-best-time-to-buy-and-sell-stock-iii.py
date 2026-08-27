# ─────────────────────────────────────────────────
#  Problem : 0123. Best Time to Buy and Sell Stock III
#  Difficulty : Hard
#  Runtime  : 0 ms
#  Memory   : 19.3 MB
#  Solved   : 2026-08-27
# ─────────────────────────────────────────────────

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        def recur(i,status,buys):
            if i==n or buys==3:
                return 0
            if status==1:
                skip=recur(i+1,status,buys)
                sell=recur(i+1,0,buys)+prices[i]
                return max(skip,sell)
            else:
                skip=recur(i+1,status,buys)
                buy=recur(i+1,1,buys+1)-prices[i]
                return max(skip,buy)
        return recur(0,0,0)