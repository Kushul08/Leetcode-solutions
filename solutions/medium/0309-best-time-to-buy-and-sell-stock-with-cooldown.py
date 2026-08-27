# ─────────────────────────────────────────────────
#  Problem : 0309. Best Time to Buy and Sell Stock with Cooldown
#  Difficulty : Medium
#  Runtime  : 3 ms
#  Memory   : 19.3 MB
#  Solved   : 2026-08-27
# ─────────────────────────────────────────────────

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)

        dp=[0,0]
        next2=[0,0]
        next1=[0,0]
        for i in range(n-1,-1,-1):
            curr=[0,0]
            for status in range(2):
                if status==1:
                    skip=next1[status]
                    sell=next2[0]+prices[i]
                    curr[status]=max(skip,sell)
                else:
                    skip=next1[status]
                    buy=next1[1]-prices[i]
                    curr[status]=max(skip,buy)
            next2=next1
            next1=curr
        return curr[0]