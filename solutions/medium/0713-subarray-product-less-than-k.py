# ─────────────────────────────────────────────────
#  Problem : 0713. Subarray Product Less Than K
#  Difficulty : Medium
#  Runtime  : 16 ms
#  Memory   : 21.4 MB
#  Solved   : 2026-09-01
# ─────────────────────────────────────────────────

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1: return 0
        n=len(nums)
        l=0
        prod=1
        count=0
        for r in range(n):
            prod*=nums[r]
            while prod>=k:
                prod=prod//nums[l]
                l+=1
            count+=(r-l+1)
        return count