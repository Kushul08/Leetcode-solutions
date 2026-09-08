# ─────────────────────────────────────────────────
#  Problem : 3870. Count Commas in Range
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 19.1 MB
#  Solved   : 2026-09-08
# ─────────────────────────────────────────────────

class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        return n-999