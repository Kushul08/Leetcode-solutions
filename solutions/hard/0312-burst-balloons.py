# ─────────────────────────────────────────────────
#  Problem : 0312. Burst Balloons
#  Difficulty : Hard
#  Runtime  : 4009 ms
#  Memory   : 48.9 MB
#  Solved   : 2026-08-30
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0,1)
        nums.append(1)
        
        @lru_cache(None)
        def recur(i,j):
            if i>j:
                return 0
            maxi=float('-inf')
            for indx in range(i,j+1):
                steps=nums[i-1]*nums[indx]*nums[j+1]+recur(i,indx-1)+recur(indx+1,j)
                maxi=max(maxi,steps)
            return maxi
        return recur(1,len(nums)-2)