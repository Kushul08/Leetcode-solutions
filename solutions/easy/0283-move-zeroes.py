# ─────────────────────────────────────────────────
#  Problem : 0283. Move Zeroes
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-09-01
# ─────────────────────────────────────────────────

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero=nums.index(0)
        for non_zero in range(len(nums)):
            if nums[non_zero]!=0:
                nums[zero],nums[non_zero]=nums[non_zero],nums[zero]
                while zero<len(nums) and nums[zero]!=0:
                    zero+=1
