# ─────────────────────────────────────────────────
#  Problem : 0128. Longest Consecutive Sequence
#  Difficulty : Medium
#  Runtime  : 50 ms
#  Memory   : 36.5 MB
#  Solved   : 2026-09-02
# ─────────────────────────────────────────────────

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        nums_set=set(nums)
        max_len=1
        for num in nums_set:
            if (num+1) not in nums_set:
                length=1
                val=num
                while (val-1) in nums_set:
                    val-=1
                    length+=1
                max_len=max(max_len,length)
        return max_len