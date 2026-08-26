# ─────────────────────────────────────────────────
#  Problem : 0122. Best Time to Buy and Sell Stock II
#  Difficulty : Medium
#  Runtime  : 43 ms
#  Memory   : 31.8 MB
#  Solved   : 2026-08-26
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n=len(prices)
        dp=[[-1]*2 for _ in range(n)]
        def recur(i,status):
            if i==n:
                return 0
            if dp[i][status]!=-1:
                return dp[i][status]
            if status==1:
                skip=recur(i+1,status)
                sell=recur(i+1,0)+prices[i]
                dp[i][status]=max(skip,sell)
                return dp[i][status] 
            else:
                skip=recur(i+1,status)
                buy=recur(i+1,1)-prices[i]
                dp[i][status]=max(skip,buy)
                return dp[i][status] 

        return recur(0,0)