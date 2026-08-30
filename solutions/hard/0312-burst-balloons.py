# ─────────────────────────────────────────────────
#  Problem : 0312. Burst Balloons
#  Difficulty : Hard
#  Runtime  : 0 ms
#  Memory   : 19.4 MB
#  Solved   : 2026-08-30
# ─────────────────────────────────────────────────

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.insert(0,1)
        nums.append(1)
        # print(nums)
        def recur(i,j):
            if i>j:
                return 0
            maxi=float('-inf')
            for indx in range(i,j+1):
                steps=nums[i-1]*nums[indx]*nums[j+1]+recur(i,indx-1)+recur(indx+1,j)
                maxi=max(maxi,steps)
            return maxi
        return recur(1,len(nums)-2)