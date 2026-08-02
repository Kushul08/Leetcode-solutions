# ─────────────────────────────────────────────────
#  Problem : 0877. Stone Game
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.4 MB
#  Solved   : 2026-08-02
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache()
        def recur(i,j,diff,turn):
            if i==j:
                if turn:
                    return diff+piles[i]
                else:
                    return diff-piles[j]
            if turn:
                return max( recur(i+1,j,diff+piles[i],False),
                recur(i,j-1,diff+piles[j],False))
            else:
                return min(recur(i+1,j,diff-piles[i],True),
                recur(i,j-1,diff-piles[j],True))
        return recur(0,0,0,True)>0
            