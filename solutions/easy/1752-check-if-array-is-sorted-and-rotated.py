# ─────────────────────────────────────────────────
#  Problem : 1752. Check if Array Is Sorted and Rotated
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-05-23
# ─────────────────────────────────────────────────

class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        prev=nums[-1]
        start=None
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<=prev:
                prev=nums[i]
            else:
                start=i+1 
                break
        if start==None: return True
        if nums[-1]>nums[0]: return False
        for i in range(start):
            if prev<=nums[i]:
                prev=nums[i]
            else:
                return False
        return True