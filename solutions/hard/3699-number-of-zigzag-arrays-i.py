# ─────────────────────────────────────────────────
#  Problem : 3699. Number of ZigZag Arrays I
#  Difficulty : Hard
#  Runtime  : 8577 ms
#  Memory   : 20.2 MB
#  Solved   : 2026-06-23
# ─────────────────────────────────────────────────

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD=int(1e9+7)
        m=r-l+1

        dp_0=[1]*m
        dp_1=[1]*m

        for _ in range(n-1):
            sum_0=list(accumulate(dp_0,initial=0))
            sum_1=list(accumulate(dp_1,initial=0))

            dp_0=[x%MOD for x in sum_1[:-1]]

            s_0_m=sum_0[-1]

            dp_1=[(s_0_m-x)%MOD for x in sum_0[1:]]
        return (sum(dp_0)+sum(dp_1))%MOD