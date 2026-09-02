# ─────────────────────────────────────────────────
#  Problem : 1011. Capacity To Ship Packages Within D Days
#  Difficulty : Medium
#  Runtime  : 254 ms
#  Memory   : 23.8 MB
#  Solved   : 2026-09-02
# ─────────────────────────────────────────────────

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def recur(threshold):
            count=0
            weight=0
            for num in weights:
                if num+weight>threshold:
                    count+=1
                    weight=0
                weight+=num
            return count
        low=max(weights)
        high=sum(weights)
        ans=0
        while low<=high:

            mid=(low+high)>>1

            if recur(mid)>=days:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return low