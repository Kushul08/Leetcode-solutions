# ─────────────────────────────────────────────────
#  Problem : 0121. Best Time to Buy and Sell Stock
#  Difficulty : Easy
#  Runtime  : 79 ms
#  Memory   : 28.6 MB
#  Solved   : 2026-08-26
# ─────────────────────────────────────────────────

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        stack=[]
        ans=0
        for i in range(n-1,-1,-1):
            while stack and stack[-1]<=prices[i]:
                stack.pop()
            if stack:
                ans=max(ans,stack[-1]-prices[i])
            else:
                stack.append(prices[i])
        return ans