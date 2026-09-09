# ─────────────────────────────────────────────────
#  Problem : 3871. Count Commas in Range II
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.3 MB
#  Solved   : 2026-09-09
# ─────────────────────────────────────────────────

class Solution:
    def countCommas(self, n: int) -> int:
        ans=0
        if n<999:
            return 0
        if n>=pow(10,15):
            ans+=(n-10**15+1)*5
            n=10**15-1
        if n>=10**12:
            ans+=(n-10**12+1)*4
            n=10**12-1
        if n>=10**9:
            ans+=(n-10**9+1)*3
            n=10**9-1
        if n>=10**6:
            ans+=(n-10**6+1)*2
            n=10**6-1
        if n>=10**3:
            ans+=(n-10**3+1)
            n=10**3-1
        return ans