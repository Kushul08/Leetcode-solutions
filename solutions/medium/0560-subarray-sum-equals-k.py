# ─────────────────────────────────────────────────
#  Problem : 0560. Subarray Sum Equals K
#  Difficulty : Medium
#  Runtime  : 42 ms
#  Memory   : 23.8 MB
#  Solved   : 2026-09-01
# ─────────────────────────────────────────────────

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        hashmap=defaultdict(int)
        hashmap[0]=1
        count=0
        l=0
        ans=0
        for r in range(n):
            ans+=nums[r]
            needed=ans-k
            count+=hashmap[needed] #defaultdicts check is key is absence asigns it to 0
            hashmap[ans]+=1
        return count