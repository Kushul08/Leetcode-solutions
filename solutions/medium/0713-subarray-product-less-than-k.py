# ─────────────────────────────────────────────────
#  Problem : 0713. Subarray Product Less Than K
#  Difficulty : Medium
#  Runtime  : 30 ms
#  Memory   : 21.3 MB
#  Solved   : 2026-09-01
# ─────────────────────────────────────────────────

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1: return 0
        n=len(nums)
        l=r=0
        prod=1
        count=0
        while r<n:
            prod*=nums[r]
            while prod>=k:
                prod=prod//nums[l]
                l+=1
            count+=(r-l+1)
            r+=1 
        return count