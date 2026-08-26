# ─────────────────────────────────────────────────
#  Problem : 0121. Best Time to Buy and Sell Stock
#  Difficulty : Easy
#  Runtime  : 64 ms
#  Memory   : 28.5 MB
#  Solved   : 2026-08-26
# ─────────────────────────────────────────────────

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        max_val=prices[-1]
        ans=0
        for i in range(n-1,-1,-1):
            ans=max(ans,max_val-prices[i])
            max_val=max(max_val,prices[i])
        return ans