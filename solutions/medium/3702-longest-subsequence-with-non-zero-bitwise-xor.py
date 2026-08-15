# ─────────────────────────────────────────────────
#  Problem : 3702. Longest Subsequence With Non-Zero Bitwise XOR
#  Difficulty : Medium
#  Runtime  : 61 ms
#  Memory   : 22.7 MB
#  Solved   : 2026-08-15
# ─────────────────────────────────────────────────

class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor=0
        n=len(nums)
        non_zero=False
        for num in nums:
            xor^=num
            if num!=0: non_zero=True
            
        if xor!=0:
            return n
        elif non_zero:
            return n-1
        return 0