# ─────────────────────────────────────────────────
#  Problem : 0714. Best Time to Buy and Sell Stock with Transaction Fee
#  Difficulty : Medium
#  Runtime  : 90 ms
#  Memory   : 26.2 MB
#  Solved   : 2026-08-27
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)

        dp=[0]*2 

        for i in range(n-1,-1,-1):
            temp=[0,0]
            skip=dp[1]
            sell=dp[0]+prices[i]-fee
            temp[1]=max(skip,sell)

            skip=dp[0]
            buy=dp[1]-prices[i]
            temp[0]=max(skip,buy)
            dp=temp
        return dp[0]
        