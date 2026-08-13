# ─────────────────────────────────────────────────
#  Problem : 0494. Target Sum
#  Difficulty : Medium
#  Runtime  : 491 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-08-13
# ─────────────────────────────────────────────────

class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        required=(target+sum(nums))/2
        def recur(i,exp):
            if i==-1:
                if exp==required:
                    return 1
                return 0
            return recur(i-1,exp+nums[i])+recur(i-1,exp)
        return recur(n-1,0)