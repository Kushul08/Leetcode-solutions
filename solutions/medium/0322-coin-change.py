# ─────────────────────────────────────────────────
#  Problem : 0322. Coin Change
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-08-11
# ─────────────────────────────────────────────────

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount==0: return 0
        coins.sort()
        target=amount
        count=0
        for i in range(len(coins)-1,-1,-1):
            if coins[i]<=target:
                needed=target/coins[i]
                target-=(coins[i]*needed)
                count+=needed
        if target==0:
            return count
        return -1