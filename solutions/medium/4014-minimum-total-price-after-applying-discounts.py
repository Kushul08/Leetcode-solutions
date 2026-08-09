# ─────────────────────────────────────────────────
#  Problem : 4014. Minimum Total Price After Applying Discounts
#  Difficulty : Medium
#  Runtime  : 187 ms
#  Memory   : 35 MB
#  Solved   : 2026-08-09
# ─────────────────────────────────────────────────

class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort()
        discounts.sort()
        n,m=len(prices),len(discounts)
        j=m-1
        total=0.00
        for i in range(n-1,-1,-1):
            if j>=0 :
                price=prices[i]*(100-discounts[j])/100
                j-=1
                total+=price
            else:
                price=prices[i]*(100-0)/100
                total+=price
        return total