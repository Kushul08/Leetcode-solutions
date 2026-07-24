# ─────────────────────────────────────────────────
#  Problem : 3514. Number of Unique XOR Triplets II
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-07-24
# ─────────────────────────────────────────────────

class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        xors=set()
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    xors.add(nums[i]^nums[j]^nums[k])
        return len(xors)