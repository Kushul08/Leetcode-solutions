# ─────────────────────────────────────────────────
#  Problem : 0122. Best Time to Buy and Sell Stock II
#  Difficulty : Medium
#  Runtime  : 7 ms
#  Memory   : 20.4 MB
#  Solved   : 2026-08-26
# ─────────────────────────────────────────────────

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n=len(prices)
        x,y=0,prices[-1]
        for i in range(n-2,-1,-1):
            temp=[0,0]
            for buy in range(2):
                if buy==1:
                    skip=y
                    sell=x+prices[i]
                    ny=max(skip,sell)
                else:
                    skip=x
                    buy=y-prices[i]
                    nx=max(skip,buy)
            x,y=nx,ny
        return x