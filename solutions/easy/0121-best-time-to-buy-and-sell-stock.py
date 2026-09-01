# ─────────────────────────────────────────────────
#  Problem : 0121. Best Time to Buy and Sell Stock
#  Difficulty : Easy
#  Runtime  : 60 ms
#  Memory   : 28.7 MB
#  Solved   : 2026-09-01
# ─────────────────────────────────────────────────

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        min_val=prices[0]
        for price in  prices:
            min_val=min(min_val,price)
            profit=max(profit,price-min_val)
        return profit