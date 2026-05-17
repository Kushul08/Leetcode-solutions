# ─────────────────────────────────────────────────
#  Problem : 0055. Jump Game
#  Difficulty : Medium
#  Runtime  : 31 ms
#  Memory   : 13.2 MB
#  Solved   : 2026-05-17
# ─────────────────────────────────────────────────

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        farrest=0

        for i in range(len(nums)):
            if farrest<i:
                return False
            farrest=max(farrest,i+nums[i])
            if farrest>=len(nums)-1:
                return True
        return True