# ─────────────────────────────────────────────────
#  Problem : 1911. Maximum Alternating Subsequence Sum
#  Difficulty : Medium
#  Runtime  : 57 ms
#  Memory   : 19.2 MB
#  Solved   : 2026-10-05
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n=len(nums)

        @lru_cache(None)
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