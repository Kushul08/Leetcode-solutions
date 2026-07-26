# ─────────────────────────────────────────────────
#  Problem : 0628. Maximum Product of Three Numbers
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-07-26
# ─────────────────────────────────────────────────

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a,b,c=float('-inf'),float('-inf'),float('-inf')
        x,y=float('inf'),float('inf')
        for num in nums:
            if num>a:
                a,b,c=num,a,b                
            elif num>b:
                b,c=num,b
            else:
                c=num
            if num<x:
                x,y=num,x
            elif num<y:
                y=num
        return max(a*b*c,a*x*y)