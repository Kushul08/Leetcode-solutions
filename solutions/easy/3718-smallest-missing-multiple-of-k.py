# ─────────────────────────────────────────────────
#  Problem : 3718. Smallest Missing Multiple of K
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.3 MB
#  Solved   : 2026-08-25
# ─────────────────────────────────────────────────

class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums_set=set(nums)
        for i in range(k,201,k):
            if i not in nums_set:
                return i
        