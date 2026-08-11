# ─────────────────────────────────────────────────
#  Problem : 2996. Smallest Missing Integer Greater Than Sequential Prefix Sum
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.3 MB
#  Solved   : 2026-08-11
# ─────────────────────────────────────────────────

from bisect import bisect_left
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
        low=sums
        high=1276
        while low<=high:
            mid=(low+high)/2
            if mid in nums_set:
                low=mid+1
            else:
                high=mid-1
        return low