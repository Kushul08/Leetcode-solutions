# ─────────────────────────────────────────────────
#  Problem : 0075. Sort Colors
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.3 MB
#  Solved   : 2026-09-01
# ─────────────────────────────────────────────────

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos=[0,0,0]
        for num in nums:
            pos[num]+=1
        indx=0
        for i in range(len(pos)):
            for j in range(pos[i]):
                nums[indx]=i
                indx+=1
        