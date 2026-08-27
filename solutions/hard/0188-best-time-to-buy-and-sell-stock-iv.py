# ─────────────────────────────────────────────────
#  Problem : 0188. Best Time to Buy and Sell Stock IV
#  Difficulty : Hard
#  Runtime  : 211 ms
#  Memory   : 99.6 MB
#  Solved   : 2026-08-27
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        @lru_cache(None)
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