# ─────────────────────────────────────────────────
#  Problem : 3731. Find Missing Elements
#  Difficulty : Easy
#  Runtime  : 1 ms
#  Memory   : 19.3 MB
#  Solved   : 2026-08-04
# ─────────────────────────────────────────────────

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini=min(nums)
        maxi=max(nums)
        seen=set(nums)
        ans=[]
        for i in range(mini,maxi+1):
            if i not in seen:
                ans.append(i)
        return ans