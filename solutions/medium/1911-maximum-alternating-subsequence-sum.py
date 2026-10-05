# ─────────────────────────────────────────────────
#  Problem : 1911. Maximum Alternating Subsequence Sum
#  Difficulty : Medium
#  Runtime  : 63 ms
#  Memory   : 19.3 MB
#  Solved   : 2026-10-05
# ─────────────────────────────────────────────────

class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        def recur(i,count):
            if i==n:
                return 0
            skip=recur(i+1,count)
            if count%2==0:
                take=recur(i+1,count+1)+nums[i]
            else:
                take=recur(i+1,count+1)-nums[i]
            return max(skip,take)
        return recur(0,0)