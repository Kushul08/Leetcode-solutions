# ─────────────────────────────────────────────────
#  Problem : 3993. Maximum Value of an Alternating Sequence
#  Difficulty : Medium
#  Runtime  : 4 ms
#  Memory   : 19.3 MB
#  Solved   : 2026-07-25
# ─────────────────────────────────────────────────

class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n==1:
            return s
        m_count=n//2
        ones_count=(n-1)//2
        return (s+m*(m_count)-ones_count) if n%2==0 else (s+m*(m_count)-ones_count)+1