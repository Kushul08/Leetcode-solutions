# ─────────────────────────────────────────────────
#  Problem : 0714. Best Time to Buy and Sell Stock with Transaction Fee
#  Difficulty : Medium
#  Runtime  : 129 ms
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
            for status in range(2):
                if status==1:
                    skip=dp[status]
                    sell=dp[0]+prices[i]-fee
                    temp[status]=max(skip,sell)
                else:
                    skip=dp[status]
                    buy=dp[1]-prices[i]
                    temp[status]=max(skip,buy)
            dp=temp
        return dp[0]
        