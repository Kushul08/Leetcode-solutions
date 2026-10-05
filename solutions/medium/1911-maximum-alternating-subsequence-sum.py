# ─────────────────────────────────────────────────
#  Problem : 1911. Maximum Alternating Subsequence Sum
#  Difficulty : Medium
#  Runtime  : 867 ms
#  Memory   : 33.7 MB
#  Solved   : 2026-10-05
# ─────────────────────────────────────────────────

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n=len(nums)

        dp=[0]*2
        for i in range(n-1,-1,-1):
            temp=[0,0]
            for sign in (0,1):
                skip=dp[sign]
                if sign%2==0:
                    take=dp[1]+nums[i]
                else:
                    take=dp[0]-nums[i]

                temp[sign]=max(skip,take)
            dp=temp
        return dp[0]