# ─────────────────────────────────────────────────
#  Problem : 0122. Best Time to Buy and Sell Stock II
#  Difficulty : Medium
#  Runtime  : 11 ms
#  Memory   : 20.3 MB
#  Solved   : 2026-08-26
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n=len(prices)
        dp=[0,prices[-1]]
        for i in range(n-2,-1,-1):
            temp=[0,0]
            for buy in range(2):
                if buy==1:
                    skip=dp[1]
                    sell=dp[0]+prices[i]
                    temp[1]=max(skip,sell)
                else:
                    skip=dp[0]
                    buy=dp[1]-prices[i]
                    temp[0]=max(skip,buy)
            dp=temp
        return dp[0]