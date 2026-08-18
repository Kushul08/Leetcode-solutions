# ─────────────────────────────────────────────────
#  Problem : 3471. Find the Largest Almost Missing Integer
#  Difficulty : Easy
#  Runtime  : 4 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-08-18
# ─────────────────────────────────────────────────

class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        if n==k: return max(nums)
        arr=[0]*51
        for i in range(len(nums)-k+1):
            for j in range(i,i+k):
                arr[nums[j]]+=1
        for i in range(50,-1,-1):
            if arr[i]==1:
                return i
        return -1