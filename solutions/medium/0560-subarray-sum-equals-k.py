# ─────────────────────────────────────────────────
#  Problem : 0560. Subarray Sum Equals K
#  Difficulty : Medium
#  Runtime  : 41 ms
#  Memory   : 22.1 MB
#  Solved   : 2026-09-01
# ─────────────────────────────────────────────────

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        hashmap=defaultdict(int)
        hashmap[0]=1
        count=0
        l=r=0
        ans=0
        while r<n:
            ans+=nums[r]
            needed=ans-k
            if needed in hashmap:
                count+=hashmap[needed] 
            hashmap[ans]+=1
            r+=1
        return count