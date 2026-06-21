# ─────────────────────────────────────────────────
#  Problem : 3969. Valid Subarrays With Matching Sum Digits I
#  Difficulty : Medium
#  Runtime  : 5121 ms
#  Memory   : 12.6 MB
#  Solved   : 2026-06-21
# ─────────────────────────────────────────────────

class Solution(object):
    def countValidSubarrays(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        count=0
        for i in range(len(nums)):
            sums=0
            for j in range(i,len(nums)):
                sums+=nums[j]
                if sums%10==x and int(str(sums)[0])==x:
                    count+=1
        return count