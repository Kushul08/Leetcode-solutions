# ─────────────────────────────────────────────────
#  Problem : 3737. Count Subarrays With Majority Element I
#  Difficulty : Medium
#  Runtime  : 2128 ms
#  Memory   : 12.6 MB
#  Solved   : 2026-06-25
# ─────────────────────────────────────────────────

class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count=0
        for i in range(len(nums)):
            freq=0
            for j in range(i,len(nums)):
                if nums[j]==target: freq+=1
                if freq>(j-i+1)//2:
                    count+=1
        return count