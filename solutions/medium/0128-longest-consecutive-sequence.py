# ─────────────────────────────────────────────────
#  Problem : 0128. Longest Consecutive Sequence
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.5 MB
#  Solved   : 2026-09-02
# ─────────────────────────────────────────────────

from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashmap=Counter(nums)
        print(hashmap)
        max_len=1
        for num in nums:
            if (num+1) not in nums:
                length=1
                val=num
                while (val-1) in hashmap:
                    val-=1
                    length+=1
                max_len=max(max_len,length)
        return max_len