# ─────────────────────────────────────────────────
#  Problem : 0122. Best Time to Buy and Sell Stock II
#  Difficulty : Medium
#  Runtime  : 23 ms
#  Memory   : 22.3 MB
#  Solved   : 2026-08-26
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n=len(prices)
        dp=[[0]*2 for _ in range(n)]
        dp[-1][0]=0
        dp[-1][1]=prices[-1]
        flag=0
        for i in range(n-2,-1,-1):
            skip=dp[i+1][1]
            sell=dp[i+1][0]+prices[i]
            dp[i][1]=max(skip,sell)
            
            skip=dp[i+1][0]
            buy=dp[i+1][1]-prices[i]
            dp[i][0]=max(skip,buy)
        return dp[0][0]