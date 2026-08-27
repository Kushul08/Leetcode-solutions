# ─────────────────────────────────────────────────
#  Problem : 0714. Best Time to Buy and Sell Stock with Transaction Fee
#  Difficulty : Medium
#  Runtime  : 61 ms
#  Memory   : 26 MB
#  Solved   : 2026-08-27
# ─────────────────────────────────────────────────

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)

        x,y=0,0
        for i in range(n-1,-1,-1):
            nx,ny=0,0
            skip=y
            sell=x+prices[i]-fee
            ny=max(skip,sell)

            skip=x
            buy=y-prices[i]
            nx=max(skip,buy)
            x,y=nx,ny
        return x
        