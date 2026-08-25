# ─────────────────────────────────────────────────
#  Problem : 3718. Smallest Missing Multiple of K
#  Difficulty : Easy
#  Runtime  : 4 ms
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
        ans=k
        while ans in nums_set:
            ans+=k
        return ans