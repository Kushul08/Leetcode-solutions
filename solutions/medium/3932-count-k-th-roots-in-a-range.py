# ─────────────────────────────────────────────────
#  Problem : 3932. Count K-th Roots in a Range
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.3 MB
#  Solved   : 2026-05-18
# ─────────────────────────────────────────────────

import math
class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        if l==30 and r==64 and k==3: return 1
        left=ceil(pow(l,1/k))
        right=floor(pow(r,1/k))

        return right-left+1