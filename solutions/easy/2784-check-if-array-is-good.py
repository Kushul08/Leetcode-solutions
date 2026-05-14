# ─────────────────────────────────────────────────
#  Problem : 2784. Check if Array is Good
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-05-14
# ─────────────────────────────────────────────────

class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_val=max(nums)
        total_sum=(max_val*(max_val+1))/2
        total_sum+=max_val
        return sum(nums)==total_sum