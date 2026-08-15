# ─────────────────────────────────────────────────
#  Problem : 3702. Longest Subsequence With Non-Zero Bitwise XOR
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 20 MB
#  Solved   : 2026-08-15
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:

        n=len(nums)

        @lru_cache(None)
        def recur(i,xor):
            if i==n:
                if xor!=0:
                    return 0
                return float('-inf')
            pick=recur(i+1,xor^nums[i])+1
            unpick=recur(i+1,xor)

            return max(pick,unpick)
        
        return recur(0,0)