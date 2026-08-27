# ─────────────────────────────────────────────────
#  Problem : 0123. Best Time to Buy and Sell Stock III
#  Difficulty : Hard
#  Runtime  : 1820 ms
#  Memory   : 797.6 MB
#  Solved   : 2026-08-27
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)

        @lru_cache(None)
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