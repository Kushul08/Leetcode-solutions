# ─────────────────────────────────────────────────
#  Problem : 0309. Best Time to Buy and Sell Stock with Cooldown
#  Difficulty : Medium
#  Runtime  : 1 ms
#  Memory   : 19.7 MB
#  Solved   : 2026-08-27
# ─────────────────────────────────────────────────

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)

        dp=[[0]*2 for _ in range(n+2)]
        for i in range(n-1,-1,-1):
            for status in range(2):
                if status==1:
                    skip=dp[i+1][status]
                    sell=dp[i+2][0]+prices[i]
                    dp[i][status]=max(skip,sell)
                else:
                    skip=dp[i+1][status]
                    buy=dp[i+1][1]-prices[i]
                    dp[i][status]=max(skip,buy)
        return dp[0][0]