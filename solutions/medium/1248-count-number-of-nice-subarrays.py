# ─────────────────────────────────────────────────
#  Problem : 1248. Count Number of Nice Subarrays
#  Difficulty : Medium
#  Runtime  : 179 ms
#  Memory   : 24.6 MB
#  Solved   : 2026-09-01
# ─────────────────────────────────────────────────

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        def recur(k):
            l=0
            r=0
            odd=0
            count=0
            ans=0
            while r<n:
                if nums[r]%2==1:
                    odd+=1
                while odd>k:
                    if nums[l]%2==1:
                        odd-=1
                    l+=1
                if odd<=k:
                    count+=(r-l+1)
                r+=1
            return count
        return recur(k)-recur(k-1)