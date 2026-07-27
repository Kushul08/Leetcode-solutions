# ─────────────────────────────────────────────────
#  Problem : 1464. Maximum Product of Two Elements in an Array
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-07-27
# ─────────────────────────────────────────────────

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_1=0
        max_2=0
        for num in nums:
            if num>max_1:
                max_1,max_2=num,max_1
            elif num>max_2:
                max_2=num
        return (max_1-1)*(max_2-1)   