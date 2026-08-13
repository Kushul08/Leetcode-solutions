# ─────────────────────────────────────────────────
#  Problem : 0494. Target Sum
#  Difficulty : Medium
#  Runtime  : 95 ms
#  Memory   : 53.5 MB
#  Solved   : 2026-08-13
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        if (target+sum(nums))%2!=0: return 0
        required=(target+sum(nums))/2

        @lru_cache(None)
        def recur(i,exp):
            if i==-1:
                if exp==0:
                    return 1
                return 0
            pick=0
            if nums[i]<=exp:
                pick=recur(i-1,exp-nums[i])
            unpick=recur(i-1,exp)
            return pick+unpick
            
        return recur(n-1,required)