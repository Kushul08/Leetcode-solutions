# ─────────────────────────────────────────────────
#  Problem : 3876. Construct Uniform Parity Array II
#  Difficulty : Medium
#  Runtime  : 19 ms
#  Memory   : 35.3 MB
#  Solved   : 2026-09-03
# ─────────────────────────────────────────────────

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if min(nums1)%2==1:
            return True
        even=0
        odd=0
        for num in nums1:#we do this to check only if there exits any odd if so we return False
            if num%2==1:
                return False
        return True