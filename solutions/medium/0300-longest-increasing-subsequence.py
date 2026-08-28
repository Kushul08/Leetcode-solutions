# ─────────────────────────────────────────────────
#  Problem : 0300. Longest Increasing Subsequence
#  Difficulty : Medium
#  Runtime  : 3860 ms
#  Memory   : 147.4 MB
#  Solved   : 2026-08-28
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)

        dp=[[0]*(n+1) for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for prev in range(-1,i):
                pick=0
                if prev==-1 or nums[prev]<nums[i]:
                    pick=dp[i+1][i+1]+1
                unpick=dp[i+1][prev+1]
                dp[i][prev+1]=max(pick,unpick)
        return dp[0][0]