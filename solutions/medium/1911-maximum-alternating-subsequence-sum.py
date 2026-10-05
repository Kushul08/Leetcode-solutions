# ─────────────────────────────────────────────────
#  Problem : 1911. Maximum Alternating Subsequence Sum
#  Difficulty : Medium
#  Runtime  : 1274 ms
#  Memory   : 97.4 MB
#  Solved   : 2026-10-05
# ─────────────────────────────────────────────────

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n=len(nums)

        dp=[[-1]*2 for _ in range(n)]
        def recur(i,sign):
            if i==n:
                return 0
            if dp[i][sign]!=-1:
                return dp[i][sign]
            skip=recur(i+1,sign)
            if sign%2==0:
                take=recur(i+1,1)+nums[i]
            else:
                take=recur(i+1,0)-nums[i]
            dp[i][sign]=max(skip,take)
            return dp[i][sign]
        return recur(0,0)