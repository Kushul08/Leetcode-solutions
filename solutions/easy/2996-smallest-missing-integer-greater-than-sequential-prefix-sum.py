# ─────────────────────────────────────────────────
#  Problem : 2996. Smallest Missing Integer Greater Than Sequential Prefix Sum
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-08-11
# ─────────────────────────────────────────────────

class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums=nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]+1==nums[i]:
                sums+=nums[i]
            else:
                break
        nums_set=set(nums)
        while sums in nums_set:
            sums+=1
        return sums