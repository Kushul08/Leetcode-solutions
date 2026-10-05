# ─────────────────────────────────────────────────
#  Problem : 1911. Maximum Alternating Subsequence Sum
#  Difficulty : Medium
#  Runtime  : 1497 ms
#  Memory   : 438.6 MB
#  Solved   : 2026-10-05
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n=len(nums)

        # dp=[[-1]*n for _ in range(n)]
        @lru_cache(None)
        def recur(i,sign):
            if i==n:
                return 0
            # if dp[i][sign]!=-1:
            #     return dp[i][sign]
            skip=recur(i+1,sign)
            if sign%2==0:
                take=recur(i+1,1)+nums[i]
            else:
                take=recur(i+1,0)-nums[i]
            # dp[i][sign]=max(skip,take)
            return max(skip,take)
        return recur(0,0)