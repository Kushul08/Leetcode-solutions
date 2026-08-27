# ─────────────────────────────────────────────────
#  Problem : 0188. Best Time to Buy and Sell Stock IV
#  Difficulty : Hard
#  Runtime  : 49 ms
#  Memory   : 19.2 MB
#  Solved   : 2026-08-27
# ─────────────────────────────────────────────────

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0 for _ in range(k+1)]
                for _ in range(2)]
        for i in range(n-1,-1,-1):
            temp=[[0 for _ in range(k+1)]
                    for _ in range(2)]
            for status in range(2):
                for cap in range(1,k+1):
                    if status==1:
                        skip=dp[status][cap]
                        sell=dp[0][cap-1]+prices[i]
                        temp[status][cap]=max(skip,sell)
                    else:
                        skip=dp[status][cap]
                        buy=dp[1][cap]-prices[i]
                        temp[status][cap]=max(skip,buy)
            dp=temp
        return dp[0][k]