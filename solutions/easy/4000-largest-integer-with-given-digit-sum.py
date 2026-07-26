# ─────────────────────────────────────────────────
#  Problem : 4000. Largest Integer With Given Digit Sum
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 19.3 MB
#  Solved   : 2026-07-26
# ─────────────────────────────────────────────────

class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s==0:
            return 0
        num=0
        sums=0
        dup_s=s
        for _ in range(n):
            for i in range(9,-1,-1):
                if i<=dup_s:
                    dup_s-=i
                    num=num*10+i
                    sums+=i
                    break
        if sums==s:
            return num
        return -1