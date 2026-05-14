# ─────────────────────────────────────────────────
#  Problem : 2784. Check if Array is Good
#  Difficulty : Easy
#  Runtime  : 4 ms
#  Memory   : 12.2 MB
#  Solved   : 2026-05-14
# ─────────────────────────────────────────────────

class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_val=max(nums)
        for i in range(1,max_val+1):
            if i not in nums:
                return False
        total_sum=(max_val*(max_val+1))/2
        total_sum+=max_val
        return sum(nums)==total_sum