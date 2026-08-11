# ─────────────────────────────────────────────────
#  Problem : 0322. Coin Change
#  Difficulty : Medium
#  Runtime  : 2458 ms
#  Memory   : 671.2 MB
#  Solved   : 2026-08-11
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n=len(coins)
        
        @lru_cache(None)
        def recur(i,target):
            if i==-1:
                if target==0:
                    return 0
                return float('inf')
            pick=float('inf')
            pick_stay=float('inf')
            if coins[i]<=target:
                pick=recur(i-1,target-coins[i])+1
                pick_stay=recur(i,target-coins[i])+1
            unpick=recur(i-1,target)

            return min(pick,unpick,pick_stay)
        coin_change=recur(n-1,amount)
        if coin_change!=float('inf'):
            return coin_change
        return -1