# ─────────────────────────────────────────────────
#  Problem : 1911. Maximum Alternating Subsequence Sum
#  Difficulty : Medium
#  Runtime  : 70 ms
#  Memory   : 27.3 MB
#  Solved   : 2026-10-05
# ─────────────────────────────────────────────────

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n=len(nums)

        dp=[[-1]*n for _ in range(n)]
        def recur(i,count):
            if i==n:
                return 0
            if dp[i][count]!=-1:
                return dp[i][count]
            skip=recur(i+1,count)
            if count%2==0:
                take=recur(i+1,count+1)+nums[i]
            else:
                take=recur(i+1,count+1)-nums[i]
            dp[i][count]=max(skip,take)
            return dp[i][count]
        return recur(0,0)