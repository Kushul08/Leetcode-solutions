# ─────────────────────────────────────────────────
#  Problem : 1043. Partition Array for Maximum Sum
#  Difficulty : Medium
#  Runtime  : 1397 ms
#  Memory   : 21.3 MB
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
            for j in range(i,i+min(k,n-i+1)):
                steps=(max(arr[i:j+1])*(j-i+1))+recur(j+1)
                maxi=max(maxi,steps)
            return maxi
        return recur(0)