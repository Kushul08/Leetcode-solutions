# ─────────────────────────────────────────────────
#  Problem : 0045. Jump Game II
#  Difficulty : Medium
#  Runtime  : 6 ms
#  Memory   : 13 MB
#  Solved   : 2026-05-17
# ─────────────────────────────────────────────────

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jump=l=r=0
        while r<len(nums)-1:
            farthest=0
            for i in range(l,r+1):
                farthest=max(farthest,nums[i]+i)
            l=r+1
            r=farthest
            jump+=1
        return jump