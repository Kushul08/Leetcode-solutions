# ─────────────────────────────────────────────────
#  Problem : 0001. Two Sum
#  Difficulty : Easy
#  Runtime  : 2 ms
#  Memory   : 13.2 MB
#  Solved   : 2026-05-12
# ─────────────────────────────────────────────────

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={nums[0]:0}
        for i in range(1,len(nums)):
            if target-nums[i] in seen:
                return [seen[target-nums[i]],i]
            seen[nums[i]]=i