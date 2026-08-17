# ─────────────────────────────────────────────────
#  Problem : 1563. Stone Game V
#  Difficulty : Hard
#  Runtime  : 27 ms
#  Memory   : 20.9 MB
#  Solved   : 2026-08-17
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n=len(stoneValue)
        if n<2:
            return 0
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=prefix[i]+stoneValue[i]

        @lru_cache(None)
        def recur(l,r):
            if r-l+1<2:
                return 0
            ans=0
            for k in range(l,r):
                left_sum=prefix[k+1]-prefix[l]
                right_sum=prefix[r+1]-prefix[k+1]

                if left_sum<right_sum:
                    curr=recur(l,k)+left_sum
                elif right_sum<left_sum:
                    curr=recur(k+1,r)+right_sum
                else:
                    curr=left_sum+max(recur(l,k),recur(k+1,r))
                ans=max(ans,curr)
            return ans
        return recur(0,n-1)