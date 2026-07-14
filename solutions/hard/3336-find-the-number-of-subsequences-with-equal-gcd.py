# ─────────────────────────────────────────────────
#  Problem : 3336. Find the Number of Subsequences With Equal GCD
#  Difficulty : Hard
#  Runtime  : 3306 ms
#  Memory   : 637.7 MB
#  Solved   : 2026-07-14
# ─────────────────────────────────────────────────

from functools import cache
class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD=int(1e9+7)
        @cache
        def subsequence(i,g1,g2):
            if i==len(nums):
                if g1==g2 and g1!=0:
                    return 1
                return 0

            seq1=subsequence(i+1,math.gcd(g1,nums[i]),g2)
            seq2=subsequence(i+1,g1,math.gcd(g2,nums[i]))
            ignore=subsequence(i+1,g1,g2)
            return seq1+seq2+ignore%MOD
        return subsequence(0,0,0)%MOD