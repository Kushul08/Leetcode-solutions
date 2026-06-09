# ─────────────────────────────────────────────────
#  Problem : 3689. Maximum Total Subarray Value I
#  Difficulty : Medium
#  Runtime  : 23 ms
#  Memory   : 16.2 MB
#  Solved   : 2026-06-09
# ─────────────────────────────────────────────────

class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return (max(nums)-min(nums))*k