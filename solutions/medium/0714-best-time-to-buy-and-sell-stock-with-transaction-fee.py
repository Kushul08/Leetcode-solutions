# ─────────────────────────────────────────────────
#  Problem : 0714. Best Time to Buy and Sell Stock with Transaction Fee
#  Difficulty : Medium
#  Runtime  : 232 ms
#  Memory   : 30.1 MB
#  Solved   : 2026-08-27
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)

        dp=[[0]*2 for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            for status in range(2):
                if status==1:
                    skip=dp[i+1][status]
                    sell=dp[i+1][0]+prices[i]-fee
                    dp[i][status]=max(skip,sell)
                else:
                    skip=dp[i+1][status]
                    buy=dp[i+1][1]-prices[i]
                    dp[i][status]=max(skip,buy)
        return dp[0][0]
        