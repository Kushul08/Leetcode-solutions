# ─────────────────────────────────────────────────
#  Problem : 0992. Subarrays with K Different Integers
#  Difficulty : Hard
#  Runtime  : 141 ms
#  Memory   : 22 MB
#  Solved   : 2026-09-01
# ─────────────────────────────────────────────────

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n=len(nums)
        def recur(k):
            hashmap={}
            count=0
            l=0
            for r in range(n):
                hashmap[nums[r]]=hashmap.get(nums[r],0)+1
                while len(hashmap)>k:
                    hashmap[nums[l]]-=1
                    if hashmap[nums[l]]==0:
                        del hashmap[nums[l]]
                    l+=1
                if len(hashmap)<=k:
                    count+=r-l+1
            return count
        return recur(k)-recur(k-1)
