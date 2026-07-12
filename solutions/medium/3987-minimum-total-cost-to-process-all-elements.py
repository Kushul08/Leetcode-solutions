# ─────────────────────────────────────────────────
#  Problem : 3987. Minimum Total Cost to Process All Elements
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.3 MB
#  Solved   : 2026-07-12
# ─────────────────────────────────────────────────

class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        available=k
        step=1
        ans=0
        MOD=int(1e9+7)
        for num in nums:
            if num>available:
                diff=num-available
                required=math.ceil(diff/k)
                available+=(k*required)
                # print(required,ans,diff,available)
                for _ in range(required):
                    ans+=step
                    step+=1
                    ans%=MOD
            available-=num    
        return ans%MOD