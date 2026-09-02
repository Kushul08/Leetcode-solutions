# ─────────────────────────────────────────────────
#  Problem : 1482. Minimum Number of Days to Make m Bouquets
#  Difficulty : Medium
#  Runtime  : 308 ms
#  Memory   : 32.4 MB
#  Solved   : 2026-09-02
# ─────────────────────────────────────────────────

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        
        def can_make(day):
            bouquets=0
            count=0
            for bloom in bloomDay:
                if bloom<=day:
                    count+=1
                    if count==k:
                        bouquets+=1
                        count=0
                else:
                    count=0
            return bouquets
        low=min(bloomDay)
        high=max(bloomDay)
        ans=0
        while low<=high:
            mid=(low+high)>>1
            if can_make(mid)>=m:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans