# ─────────────────────────────────────────────────
#  Problem : 0188. Best Time to Buy and Sell Stock IV
#  Difficulty : Hard
#  Runtime  : 0 ms
#  Memory   : 19.4 MB
#  Solved   : 2026-08-27
# ─────────────────────────────────────────────────

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        def recur(i,status,k):
            if i==n or k==0:
                return 0
            if status==1:
                skip=recur(i+1,status,k)
                sell=recur(i+1,0,k-1)+prices[i]
                return max(skip,sell)
            else:
                skip=recur(i+1,status,k)
                buy=recur(i+1,1,k)-prices[i]
                return max(skip,buy)
        return recur(0,0,k)