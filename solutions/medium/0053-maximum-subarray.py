# ─────────────────────────────────────────────────
#  Problem : 0053. Maximum Subarray
#  Difficulty : Medium
#  Runtime  : 94 ms
#  Memory   : 21.1 MB
#  Solved   : 2026-09-01
# ─────────────────────────────────────────────────

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums=nums[0]
        max_sum=nums[0]
        for i in range(1,len(nums)):
            sums+=nums[i]
            sums=max(sums,nums[i])
            max_sum=max(max_sum,sums)
        return max_sum