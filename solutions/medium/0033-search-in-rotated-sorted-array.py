# ─────────────────────────────────────────────────
#  Problem : 0033. Search in Rotated Sorted Array
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.6 MB
#  Solved   : 2026-05-22
# ─────────────────────────────────────────────────

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low,high=0,len(nums)-1

        while low<=high:
            mid=(low+high)//2

            if nums[mid]==target:
                return mid
            elif nums[low]<=nums[mid]:
                if nums[low]<=target and target<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<=target and target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return -1