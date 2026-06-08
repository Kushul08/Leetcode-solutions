# ─────────────────────────────────────────────────
#  Problem : 2161. Partition Array According to Given Pivot
#  Difficulty : Medium
#  Runtime  : 192 ms
#  Memory   : 36.7 MB
#  Solved   : 2026-06-08
# ─────────────────────────────────────────────────

class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        left=0
        right=len(nums)-1
        ans=[pivot]*len(nums)
        for i,j in zip(range(len(nums)),range(len(nums)-1,-1,-1)):
            if nums[i]<pivot:
                ans[left]=nums[i]
                left+=1
            if nums[j]>pivot:
                ans[right]=nums[j]
                right-=1
        return ans