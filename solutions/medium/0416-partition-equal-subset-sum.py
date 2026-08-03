# ─────────────────────────────────────────────────
#  Problem : 0416. Partition Equal Subset Sum
#  Difficulty : Medium
#  Runtime  : 2544 ms
#  Memory   : 169.8 MB
#  Solved   : 2026-08-03
# ─────────────────────────────────────────────────

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if (sum(nums)&1)==1:
            return False
        n=len(nums)
        k=sum(nums)//2

        dp=[[-1]*(k+1) for _ in range(n)]
        
        def recur(i,target):
            if i==n:
                return target==0
            if target==0:
                return True
            if dp[i][target]!=-1:
                return dp[i][target]
            if nums[i]<=target:
                pick=recur(i+1,target-nums[i])
            else:
                pick=recur(i+1,target)
            unpick=recur(i+1,target)
            dp[i][target]=pick or unpick

            return dp[i][target]
        return recur(0,k)