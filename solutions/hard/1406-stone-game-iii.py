# ─────────────────────────────────────────────────
#  Problem : 1406. Stone Game III
#  Difficulty : Hard
#  Runtime  : 2327 ms
#  Memory   : 497.8 MB
#  Solved   : 2026-08-03
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        n=len(stoneValue)

        @lru_cache(None)
        def recur(i,turn):
            if i>=n:
                return 0
            if turn:
                one=recur(i+1,False)+stoneValue[i]
                two=recur(i+2,False)+stoneValue[i]+stoneValue[i+1] if i+1<n else float('-inf')
                three=recur(i+3,False)+stoneValue[i]+stoneValue[i+1]+stoneValue[i+2] if i+2<n else float('-inf')
                return max(one,two,three)
            else:
                one=recur(i+1,True)-stoneValue[i]
                two=recur(i+2,True)-stoneValue[i]-stoneValue[i+1] if i+1<n else float('inf')
                three=recur(i+3,True)-stoneValue[i]-stoneValue[i+1]-stoneValue[i+2] if i+2<n else float('inf')
                return min(one,two,three)
        value=recur(0,True)
        if value<0:
            return 'Bob'
        elif value==0:
            return 'Tie'
        else:
            return 'Alice'