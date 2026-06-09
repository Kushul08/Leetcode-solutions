# ─────────────────────────────────────────────────
#  Problem : 3689. Maximum Total Subarray Value I
#  Difficulty : Medium
#  Runtime  : 30 ms
#  Memory   : 16.3 MB
#  Solved   : 2026-06-09
# ─────────────────────────────────────────────────

class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minimum=min(nums)
        maximum=max(nums)

        return (maximum-minimum)*k