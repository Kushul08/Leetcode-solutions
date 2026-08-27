# ─────────────────────────────────────────────────
#  Problem : 0123. Best Time to Buy and Sell Stock III
#  Difficulty : Hard
#  Runtime  : 1676 ms
#  Memory   : 114.1 MB
#  Solved   : 2026-08-27
# ─────────────────────────────────────────────────

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[-1 for _ in range(4)] for _ in range(2) ] for _ in range(n)]
        def recur(i,status,buys):
            if i==n or buys==3:
                return 0
            if dp[i][status][buys]!=-1:
                return dp[i][status][buys]
            if status==1:
                skip=recur(i+1,status,buys)
                sell=recur(i+1,0,buys)+prices[i]
                dp[i][status][buys]=max(skip,sell)
                return dp[i][status][buys]
            else:
                skip=recur(i+1,status,buys)
                buy=recur(i+1,1,buys+1)-prices[i]
                dp[i][status][buys]=max(skip,buy)
                return dp[i][status][buys]
        return recur(0,0,0)