# ─────────────────────────────────────────────────
#  Problem : 0300. Longest Increasing Subsequence
#  Difficulty : Medium
#  Runtime  : 1211 ms
#  Memory   : 19.5 MB
#  Solved   : 2026-08-28
# ─────────────────────────────────────────────────

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)

        dp=[1]*(n)
        for i in range(1,n):
            max_val=dp[i]
            for j in range(0,i):
                if nums[j]<nums[i]:
                    max_val=max(dp[i]+dp[j],max_val)
            dp[i]=max_val
        return max(dp)