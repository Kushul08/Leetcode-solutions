# ─────────────────────────────────────────────────
#  Problem : 3731. Find Missing Elements
#  Difficulty : Easy
#  Runtime  : 3 ms
#  Memory   : 19.4 MB
#  Solved   : 2026-08-04
# ─────────────────────────────────────────────────

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans=[]
        i=0
        for num in range(min(nums),max(nums)):
            if num!=nums[i]:
                ans.append(num)
            else:
                i+=1
        return ans