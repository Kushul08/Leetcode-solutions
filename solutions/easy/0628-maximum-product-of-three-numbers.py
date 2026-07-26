# ─────────────────────────────────────────────────
#  Problem : 0628. Maximum Product of Three Numbers
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.3 MB
#  Solved   : 2026-07-26
# ─────────────────────────────────────────────────

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1) Just sort in ascending order and pick the last 3 
        # 2) Use the heapfy method from heapq, and pop three times, but we need to use -ve sign to get convert it to max heap from min heap
        nums.sort()
        return nums[-1]*nums[-2]*nums[-3]