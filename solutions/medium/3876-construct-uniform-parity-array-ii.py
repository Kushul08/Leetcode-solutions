# ─────────────────────────────────────────────────
#  Problem : 3876. Construct Uniform Parity Array II
#  Difficulty : Medium
#  Runtime  : 20 ms
#  Memory   : 35 MB
#  Solved   : 2026-09-03
# ─────────────────────────────────────────────────

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if min(nums1)%2==1:
            return True
        even=0
        odd=0
        for num in nums1:
            if num%2==0:
                even+=1
            else:
                odd+=1
        if odd==len(nums1) or even==len(nums1):
            return True
        return False