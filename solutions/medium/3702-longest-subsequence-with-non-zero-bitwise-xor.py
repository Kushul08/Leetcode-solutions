# ─────────────────────────────────────────────────
#  Problem : 3702. Longest Subsequence With Non-Zero Bitwise XOR
#  Difficulty : Medium
#  Runtime  : 1 ms
#  Memory   : 20.1 MB
#  Solved   : 2026-08-15
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:

        n=len(nums)

        @lru_cache(None)
        def recur(i,take,xor):
            if i==n:
                if xor!=0:
                    return take
                return 0
            pick=recur(i+1,take+1,xor^nums[i])
            unpick=recur(i+1,take,xor)

            return max(pick,unpick)
        
        return recur(0,0,0)