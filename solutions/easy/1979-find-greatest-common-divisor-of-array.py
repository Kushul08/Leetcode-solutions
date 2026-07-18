# ─────────────────────────────────────────────────
#  Problem : 1979. Find Greatest Common Divisor of Array
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-07-18
# ─────────────────────────────────────────────────

class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn=min(nums)
        mx=max(nums)
        for i in range(min(mn,mx),0,-1):
            if mn%i==0 and mx%i==0:
                return i
        return 1