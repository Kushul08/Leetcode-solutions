# ─────────────────────────────────────────────────
#  Problem : 3904. Smallest Stable Index II
#  Difficulty : Medium
#  Runtime  : 300 ms
#  Memory   : 21.6 MB
#  Solved   : 2026-09-05
# ─────────────────────────────────────────────────

class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_elements=[0]*len(nums)
        mini=nums[-1]
        for i in range(len(nums)-1,-1,-1):
            mini=min(mini,nums[i])
            min_elements[i]=mini
        maxi=nums[0]
        for i in range(len(nums)):
            maxi=max(maxi,nums[i])
            if maxi-min_elements[i]<=k:
                return i
        return -1