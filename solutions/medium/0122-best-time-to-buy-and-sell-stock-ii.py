# ─────────────────────────────────────────────────
#  Problem : 0122. Best Time to Buy and Sell Stock II
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.2 MB
#  Solved   : 2026-08-26
# ─────────────────────────────────────────────────

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n=len(prices)
        def recur(i,status):
            if i==n:
                return 0
            if status==1:
                skip=recur(i+1,status)
                sell=recur(i+1,0)+prices[i]
                return max(skip,sell)
            else:
                skip=recur(i+1,status)
                buy=recur(i+1,1)-prices[i]
                return max(skip,buy)
        return recur(0,0)