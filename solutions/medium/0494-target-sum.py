# ─────────────────────────────────────────────────
#  Problem : 0494. Target Sum
#  Difficulty : Medium
#  Runtime  : 135 ms
#  Memory   : 79.9 MB
#  Solved   : 2026-08-13
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)

        @lru_cache(None)
        def recur(i,exp):
            if i==-1:
                if exp==target:
                    return 1
                return 0
            return recur(i-1,exp+nums[i])+recur(i-1,exp-nums[i])
        return recur(n-1,0)
        