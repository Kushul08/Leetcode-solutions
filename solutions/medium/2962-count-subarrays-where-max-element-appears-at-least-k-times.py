# ─────────────────────────────────────────────────
#  Problem : 2962. Count Subarrays Where Max Element Appears at Least K Times
#  Difficulty : Medium
#  Runtime  : 249 ms
#  Memory   : 32.3 MB
#  Solved   : 2026-09-01
# ─────────────────────────────────────────────────

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        max_val=max(nums)
        freq=nums.count(max_val)
        
        def recur(k):
            l=r=0
            ans=0
            count=0
            while r<n:
                ans+=1 if nums[r]==max_val else 0
                while ans>k:
                    ans-=1 if nums[l]==max_val else 0
                    l+=1
                if ans<=k:
                    count+=(r-l+1)
                r+=1
            return count
        return recur(freq)-recur(k-1)