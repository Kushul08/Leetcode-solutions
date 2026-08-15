# ─────────────────────────────────────────────────
#  Problem : 3702. Longest Subsequence With Non-Zero Bitwise XOR
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-08-15
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:

        n=len(nums)
        dp={}
        def recur(i,xor):
            if i==n:
                if xor!=0:
                    return 0
                return float('-inf')
            if (i,xor) in dp:
                return dp[(i,xor)]
            pick=recur(i+1,xor^nums[i])+1
            unpick=recur(i+1,xor)

            dp[(i,xor)]=max(pick,unpick)
            return dp[(i,xor)]
        return recur(0,0)