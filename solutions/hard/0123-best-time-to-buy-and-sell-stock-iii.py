# ─────────────────────────────────────────────────
#  Problem : 0123. Best Time to Buy and Sell Stock III
#  Difficulty : Hard
#  Runtime  : 345 ms
#  Memory   : 30.8 MB
#  Solved   : 2026-08-27
# ─────────────────────────────────────────────────

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0 for _ in range(4)] for _ in range(2)]
        temp=[[0 for _ in range(4)] for _ in range(2)]
        
        for i in range(n-1,-1,-1):
            for status in range(2):
                for buys in range(2,0,-1):
                    if status==1:
                        skip=dp[status][buys]
                        sell=dp[0][buys-1]+prices[i]
                        temp[status][buys]=max(skip,sell)
                    else:
                        skip=dp[status][buys]
                        buy=dp[1][buys]-prices[i]
                        temp[status][buys]=max(skip,buy)
            dp=temp
        return dp[0][2]