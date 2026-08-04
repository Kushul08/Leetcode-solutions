# ─────────────────────────────────────────────────
#  Problem : 3731. Find Missing Elements
#  Difficulty : Easy
#  Runtime  : 7 ms
#  Memory   : 19.3 MB
#  Solved   : 2026-08-04
# ─────────────────────────────────────────────────

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini=min(nums)
        maxi=max(nums)
        ans=[]
        for i in range(mini,maxi+1):
            if i not in nums:
                ans.append(i)
        return ans