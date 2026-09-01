# ─────────────────────────────────────────────────
#  Problem : 0930. Binary Subarrays With Sum
#  Difficulty : Medium
#  Runtime  : 24 ms
#  Memory   : 23.2 MB
#  Solved   : 2026-09-01
# ─────────────────────────────────────────────────

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashmap={0:1}
        ans=0
        count=0
        for num in nums:
            ans+=num
            if ans-goal in hashmap:
                count+=hashmap[ans-goal]
            hashmap[ans]=hashmap.get(ans,0)+1
        return count