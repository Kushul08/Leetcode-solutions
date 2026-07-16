# ─────────────────────────────────────────────────
#  Problem : 3867. Sum of GCD of Formed Pairs
#  Difficulty : Medium
#  Runtime  : 181 ms
#  Memory   : 33.8 MB
#  Solved   : 2026-07-16
# ─────────────────────────────────────────────────

from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        max_val=nums[0]
        prefix_gcd=[]
        for num in nums:
            max_val=max(max_val,num)
            prefix_gcd.append(math.gcd(max_val,num))
        # print(prefix_gcd)
        prefix_gcd.sort()

        l=0
        r=len(nums)-1
        gcd=0
        while l<r:
            gcd+=math.gcd(prefix_gcd[l],prefix_gcd[r])
            l+=1
            r-=1
        return gcd