# ─────────────────────────────────────────────────
#  Problem : 2091. Removing Minimum and Maximum From Array
#  Difficulty : Medium
#  Runtime  : 43 ms
#  Memory   : 21.9 MB
#  Solved   : 2026-08-30
# ─────────────────────────────────────────────────

class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        min_indx=0
        max_indx=0
        mini=float('inf')
        maxi=float('-inf')
        for i in range(n):
            if nums[i]<mini:
                min_indx=i
                mini=nums[i]
            if nums[i]>maxi:
                max_indx=i
                maxi=nums[i]
        min_dels=float('inf')

        if min_indx<max_indx:
            min_dels=min(min_dels,max_indx+1)
            min_dels=min(min_dels,n-min_indx)
            min_dels=min(min_dels,min_indx+1+n-max_indx)
        else:
            min_dels=min(min_dels,min_indx+1)
            min_dels=min(min_dels,n-max_indx)
            min_dels=min(min_dels,max_indx+1+n-min_indx)
        return min_dels