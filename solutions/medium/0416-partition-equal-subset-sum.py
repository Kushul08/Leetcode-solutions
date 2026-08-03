# ─────────────────────────────────────────────────
#  Problem : 0416. Partition Equal Subset Sum
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.4 MB
#  Solved   : 2026-08-03
# ─────────────────────────────────────────────────

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if (sum(nums)&1)==1:
            return False
        n=len(nums)
        k=sum(nums)//2
        def recur(i,target):
            if i==n:
                return target==0
            if target==0:
                return True
            if nums[i]<=target:
                pick=recur(i+1,target-nums[i])
            else:
                pick=recur(i+1,target)
            unpick=recur(i+1,target)
            return pick or unpick
        return recur(0,k)