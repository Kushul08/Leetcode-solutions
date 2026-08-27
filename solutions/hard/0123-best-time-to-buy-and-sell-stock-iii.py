# ─────────────────────────────────────────────────
#  Problem : 0123. Best Time to Buy and Sell Stock III
#  Difficulty : Hard
#  Runtime  : 1046 ms
#  Memory   : 62.6 MB
#  Solved   : 2026-08-27
# ─────────────────────────────────────────────────

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[0 for _ in range(4)] 
            for _ in range(2)] 
            for _ in range(n+1)]
        
        for i in range(n-1,-1,-1):
            for status in range(2):
                for buys in range(2,-1,-1):
                    if status==1:
                        skip=dp[i+1][status][buys]
                        sell=dp[i+1][0][buys]+prices[i]
                        dp[i][status][buys]=max(skip,sell)
                    else:
                        skip=dp[i+1][status][buys]
                        buy=dp[i+1][1][buys+1]-prices[i]
                        dp[i][status][buys]=max(skip,buy)
        return dp[0][0][0]