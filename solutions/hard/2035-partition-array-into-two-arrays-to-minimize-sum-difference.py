# ─────────────────────────────────────────────────
#  Problem : 2035. Partition Array Into Two Arrays to Minimize Sum Difference
#  Difficulty : Hard
#  Runtime  : 0 ms
#  Memory   : 19.4 MB
#  Solved   : 2026-08-03
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n=len(nums)
        total_sum=sum(nums)
        min_abs=float('inf')

        @lru_cache(None)
        def recur(i,sums,take):
            nonlocal min_abs
            if i==n:
                if take==n//2:
                    rem_sum=total_sum-sums
                    min_abs=min(min_abs,abs(rem_sum-sums))
                return
            if take==n//2:
                rem_sum=total_sum-sums
                min_abs=min(min_abs,abs(rem_sum-sums))
                return
            recur(i+1,sums+nums[i],take+1)
            recur(i+1,sums,take)
            return
        recur(0,0,0)
        return min_abs