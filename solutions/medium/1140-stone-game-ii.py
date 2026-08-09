# ─────────────────────────────────────────────────
#  Problem : 1140. Stone Game II
#  Difficulty : Medium
#  Runtime  : 429 ms
#  Memory   : 34.5 MB
#  Solved   : 2026-08-09
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n=len(piles)
        alice=[0]

        @lru_cache(None)
        def recur(i,m,turn):
            if i==n:
                return 0
            
            
            if turn:
                ans=float('-inf')

                for x in range(i,min(i+2*m-1,n-1)+1):
                    stones=sum(piles[i:x+1])
                    taken=x-i+1
                    ans=max(ans,recur(x+1,max(m,taken),False)+stones)
                return ans
            else:
                ans=float('inf')

                for x in range(i,min(i+2*m-1,n-1)+1):
                    taken=x-i+1
                    ans=min(ans,recur(x+1,max(m,taken),True))
                return ans
        return recur(0,1,True)