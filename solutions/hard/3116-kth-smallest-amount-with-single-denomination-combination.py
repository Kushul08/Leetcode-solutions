# ─────────────────────────────────────────────────
#  Problem : 3116. Kth Smallest Amount With Single Denomination Combination
#  Difficulty : Hard
#  Runtime  : 0 ms
#  Memory   : 19.3 MB
#  Solved   : 2026-08-21
# ─────────────────────────────────────────────────

from sortedcontainers import SortedList
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        ans=SortedList()
        for coin in coins:
            for i in range(1,k+1):
                ans.add(coin*i)
        return ans[k]