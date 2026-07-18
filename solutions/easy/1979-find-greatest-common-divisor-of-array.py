# ─────────────────────────────────────────────────
#  Problem : 1979. Find Greatest Common Divisor of Array
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.6 MB
#  Solved   : 2026-07-18
# ─────────────────────────────────────────────────

class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a,b=min(nums),max(nums)
        while b:
            a,b=b,a%b
        return a