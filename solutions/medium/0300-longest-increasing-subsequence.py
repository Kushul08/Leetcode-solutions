# ─────────────────────────────────────────────────
#  Problem : 0300. Longest Increasing Subsequence
#  Difficulty : Medium
#  Runtime  : 371 ms
#  Memory   : 104.9 MB
#  Solved   : 2026-08-28
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)

        # dp=[[-1]*(n) for _ in range(n)]
        @lru_cache(None)
        def recur(i,prev):
            if i==n:
                return 0
            # if dp[i][prev]!=-1:
                # return dp[i][prev]
            pick=0
            if prev==-1 or nums[prev]<nums[i]:
                pick=recur(i+1,i)+1
            unpick=recur(i+1,prev)
            # dp[i][prev]=max(pick,unpick)
            # return dp[i][prev]
            return max(pick,unpick)
        return recur(0,-1)