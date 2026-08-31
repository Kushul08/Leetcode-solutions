# ─────────────────────────────────────────────────
#  Problem : 1043. Partition Array for Maximum Sum
#  Difficulty : Medium
#  Runtime  : 183 ms
#  Memory   : 21.1 MB
#  Solved   : 2026-08-31
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)
        @lru_cache(None)
        def recur(i):
            if i==n:
                return 0
            maxi=-1e9
            max_val=-1e9
            for j in range(i,min(i+k,n)):
                max_val=max(max_val,arr[j])
                steps=(max_val*(j-i+1))+recur(j+1)
                maxi=max(maxi,steps)
            return maxi
        return recur(0)