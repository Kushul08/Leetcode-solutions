# ─────────────────────────────────────────────────
#  Problem : 0714. Best Time to Buy and Sell Stock with Transaction Fee
#  Difficulty : Medium
#  Runtime  : 602 ms
#  Memory   : 274.6 MB
#  Solved   : 2026-08-27
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)

        @lru_cache(None)
        def recur(i,status):
            if i==n:
                return 0
            if status==1:
                skip=recur(i+1,status)
                sell=recur(i+1,0)+prices[i]-fee
                return max(skip,sell)
            else:
                skip=recur(i+1,status)
                buy=recur(i+1,1)-prices[i]
                return max(skip,buy)
        return recur(0,0)