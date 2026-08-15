# ─────────────────────────────────────────────────
#  Problem : 3702. Longest Subsequence With Non-Zero Bitwise XOR
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.2 MB
#  Solved   : 2026-08-15
# ─────────────────────────────────────────────────

class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        def recur(i,take,xor):
            if i==n:
                if xor!=0:
                    return take
                return 0
            pick=recur(i+1,take+1,xor^nums[i])
            unpick=recur(i+1,take,xor)

            return max(pick,unpick)
        
        return recur(0,0,0)