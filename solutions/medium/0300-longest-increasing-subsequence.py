# ─────────────────────────────────────────────────
#  Problem : 0300. Longest Increasing Subsequence
#  Difficulty : Medium
#  Runtime  : 2825 ms
#  Memory   : 19.5 MB
#  Solved   : 2026-08-28
# ─────────────────────────────────────────────────

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)

        dp=[0]*(n+1)
        for i in range(n-1,-1,-1):
            temp=[0]*(n+1)
            for prev in range(i-1,-2,-1):
                pick=0
                if prev==-1 or nums[prev]<nums[i]:
                    pick=dp[i+1]+1
                unpick=dp[prev+1]
                temp[prev+1]=max(pick,unpick)
            dp=temp
        return dp[0]