# ─────────────────────────────────────────────────
#  Problem : 0154. Find Minimum in Rotated Sorted Array II
#  Difficulty : Hard
#  Runtime  : 0 ms
#  Memory   : 12.3 MB
#  Solved   : 2026-05-16
# ─────────────────────────────────────────────────

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=len(nums)-1

        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            elif nums[mid]==nums[r]:
                l+=1
            else:
                r=mid
        return nums[l]