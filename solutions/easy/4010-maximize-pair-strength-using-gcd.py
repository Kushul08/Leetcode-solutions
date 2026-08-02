# ─────────────────────────────────────────────────
#  Problem : 4010. Maximize Pair Strength Using GCD
#  Difficulty : Easy
#  Runtime  : 4713 ms
#  Memory   : 19.5 MB
#  Solved   : 2026-08-02
# ─────────────────────────────────────────────────

from math import gcd
class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        max_ans=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                ans=nums[i]*nums[j]//pow(gcd(nums[i],nums[j]),2)
                max_ans=max(max_ans,ans)
        return max_ans