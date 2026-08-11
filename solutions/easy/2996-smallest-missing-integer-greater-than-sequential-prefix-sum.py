# ─────────────────────────────────────────────────
#  Problem : 2996. Smallest Missing Integer Greater Than Sequential Prefix Sum
#  Difficulty : Easy
#  Runtime  : 1 ms
#  Memory   : 12.4 MB
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
        for x in range(sums,1276):
            if x not in nums:
                return x 