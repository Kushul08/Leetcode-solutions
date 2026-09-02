# ─────────────────────────────────────────────────
#  Problem : 0035. Search Insert Position
#  Difficulty : Easy
#  Runtime  : 2 ms
#  Memory   : 19.9 MB
#  Solved   : 2026-09-02
# ─────────────────────────────────────────────────

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        low=0
        high=n-1

        while low<=high:
            mid=(low+high)>>1
            if nums[mid]>=target:
                high-=1
            else:
                low+=1
        return low
