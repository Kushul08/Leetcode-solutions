# ─────────────────────────────────────────────────
#  Problem : 0518. Coin Change II
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.4 MB
#  Solved   : 2026-08-13
# ─────────────────────────────────────────────────

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n=len(coins)
        
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