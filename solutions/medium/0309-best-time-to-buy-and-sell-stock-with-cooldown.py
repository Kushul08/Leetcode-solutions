# ─────────────────────────────────────────────────
#  Problem : 0309. Best Time to Buy and Sell Stock with Cooldown
#  Difficulty : Medium
#  Runtime  : 7 ms
#  Memory   : 26.1 MB
#  Solved   : 2026-08-27
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)

        @lru_cache(None)
        def recur(i,status):
            if i>=n:
                return 0
            if status==1:
                skip=recur(i+1,status)
                sell=recur(i+2,0)+prices[i]
                return max(skip,sell)
            else:
                skip=recur(i+1,status)
                buy=recur(i+1,1)-prices[i]
                return max(skip,buy)
        return recur(0,0)