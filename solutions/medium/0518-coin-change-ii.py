# ─────────────────────────────────────────────────
#  Problem : 0518. Coin Change II
#  Difficulty : Medium
#  Runtime  : 735 ms
#  Memory   : 204.3 MB
#  Solved   : 2026-08-13
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        
        @lru_cache(None)
        def recur(i,money):
            if i==-1:
                if money==0:
                    return 1
                return 0

            pick=0
            if coins[i]<=money:
                pick=recur(i,money-coins[i])
            unpick=recur(i-1,money)
            return pick+unpick
        return recur(n-1,amount)