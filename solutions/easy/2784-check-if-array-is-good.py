# ─────────────────────────────────────────────────
#  Problem : 2784. Check if Array is Good
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.3 MB
#  Solved   : 2026-05-14
# ─────────────────────────────────────────────────

class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_val=max(nums)
        if len(set(nums))!=max_val:
            return False
        if max_val+1!=len(nums):
            return False
        if nums.count(max_val)==2:
            return True
        return False