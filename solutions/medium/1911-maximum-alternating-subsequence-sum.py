# ─────────────────────────────────────────────────
#  Problem : 1911. Maximum Alternating Subsequence Sum
#  Difficulty : Medium
#  Runtime  : 998 ms
#  Memory   : 37.5 MB
#  Solved   : 2026-10-05
# ─────────────────────────────────────────────────

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n=len(nums)

        dp=[[0]*2 for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for sign in (0,1):
                skip=dp[i+1][sign]
                if sign%2==0:
                    take=dp[i+1][1]+nums[i]
                else:
                    take=dp[i+1][0]-nums[i]

                dp[i][sign]=max(skip,take)
                
        return dp[0][0]