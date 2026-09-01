# ─────────────────────────────────────────────────
#  Problem : 0930. Binary Subarrays With Sum
#  Difficulty : Medium
#  Runtime  : 43 ms
#  Memory   : 20.1 MB
#  Solved   : 2026-09-01
# ─────────────────────────────────────────────────

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n=len(nums)
        def recur(k):
            l=0
            count=0
            ans=0
            for r in range(n):
                ans+=nums[r]
                while ans>k:
                    ans-=nums[l]
                    l+=1
                if ans<=k:
                    count+=(r-l+1)
            return count
        if goal==0:
            return recur(goal)
        return recur(goal)-recur(goal-1)
