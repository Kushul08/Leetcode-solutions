# ─────────────────────────────────────────────────
#  Problem : 4039. Sum of Decoded Numbers
#  Difficulty : Medium
#  Runtime  : 447 ms
#  Memory   : 32.1 MB
#  Solved   : 2026-08-30
# ─────────────────────────────────────────────────

class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        MOD=int(1e9+7)
        ans=0
        for num in nums:
            width=num%10
            d=num//10
            x=int(str(d)[:width])
            y=int(str(d)[width:])
            ans+=pow(x,y,MOD)
        return ans%MOD