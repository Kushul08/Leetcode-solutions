# ─────────────────────────────────────────────────
#  Problem : 2091. Removing Minimum and Maximum From Array
#  Difficulty : Medium
#  Runtime  : 23 ms
#  Memory   : 20.4 MB
#  Solved   : 2026-08-30
# ─────────────────────────────────────────────────

class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        min_indx=nums.index(min(nums))
        max_indx=nums.index(max(nums))
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