# ─────────────────────────────────────────────────
#  Problem : 0494. Target Sum
#  Difficulty : Medium
#  Runtime  : 165 ms
#  Memory   : 71.7 MB
#  Solved   : 2026-08-13
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)

        dp={}     
        def recur(i,exp):
            if i==-1:
                if exp==target:
                    return 1
                return 0
            if (i,exp) in dp:
                return dp[(i,exp)]
            dp[(i,exp)]=recur(i-1,exp+nums[i])+recur(i-1,exp-nums[i])
            return dp[(i,exp)]
        return recur(n-1,0)
        