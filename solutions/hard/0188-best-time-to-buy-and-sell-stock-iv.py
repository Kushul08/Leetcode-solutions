# ─────────────────────────────────────────────────
#  Problem : 0188. Best Time to Buy and Sell Stock IV
#  Difficulty : Hard
#  Runtime  : 63 ms
#  Memory   : 22.2 MB
#  Solved   : 2026-08-27
# ─────────────────────────────────────────────────

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[0 for _ in range(k+1)]
                for _ in range(2)]
                for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for status in range(2):
                for cap in range(k,0,-1):
                    if status==1:
                        skip=dp[i+1][status][cap]
                        sell=dp[i+1][0][cap-1]+prices[i]
                        dp[i][status][cap]=max(skip,sell)
                    else:
                        skip=dp[i+1][status][cap]
                        buy=dp[i+1][1][cap]-prices[i]
                        dp[i][status][cap]=max(skip,buy)
        return dp[0][0][k]