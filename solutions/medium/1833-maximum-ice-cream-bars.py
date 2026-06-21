# ─────────────────────────────────────────────────
#  Problem : 1833. Maximum Ice Cream Bars
#  Difficulty : Medium
#  Runtime  : 104 ms
#  Memory   : 21.2 MB
#  Solved   : 2026-06-21
# ─────────────────────────────────────────────────

class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        if coins<min(costs): return 0
        arr=[0]*(max(costs)+1)
        for cost in costs:
            arr[cost]+=1
        # print(arr)
        max_ice=0

        for i in range(1,len(arr)):
            
            # print(coins,i,max_ice)
            if coins==0 or coins<i: break
            need=min(coins//i,arr[i])
            coins-=need*i
            max_ice+=need
        return max_ice