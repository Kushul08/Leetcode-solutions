# ─────────────────────────────────────────────────
#  Problem : 3987. Minimum Total Cost to Process All Elements
#  Difficulty : Medium
#  Runtime  : 321 ms
#  Memory   : 32.9 MB
#  Solved   : 2026-07-12
# ─────────────────────────────────────────────────

import math
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
                ans+=(((required+step-1)*(required+step))//2-((step*(step-1))//2))%MOD
                step+=required
            available-=num    
        # ans=int(ans)
        return ans%MOD