# ─────────────────────────────────────────────────
#  Problem : 0121. Best Time to Buy and Sell Stock
#  Difficulty : Easy
#  Runtime  : 105 ms
#  Memory   : 29 MB
#  Solved   : 2026-08-26
# ─────────────────────────────────────────────────

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        stack=[]
        next_greater=[0]*(n)
        for i in range(n-1,-1,-1):
            while stack and stack[-1]<=prices[i]:
                stack.pop()
            if stack:
                next_greater[i]=stack[-1] 
            else:
                stack.append(prices[i])
                next_greater[i]=stack[-1] 
        ans=0
        for i,price in enumerate(prices):
            ans=max(ans,next_greater[i]-prices[i])
        return ans