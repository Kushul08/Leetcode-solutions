# ─────────────────────────────────────────────────
#  Problem : 0045. Jump Game II
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-05-17
# ─────────────────────────────────────────────────

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def find_greater(start,end):
            if end>=len(nums)-1:
                return len(nums)
            farthest=0
            index=0
            for i in range(start,end):
                if farthest<i+nums[i]:
                    farthest=i+nums[i]
                    index=i
            return index
        
        i=0
        count=0
        while i<len(nums):
            i=find_greater(i+1,i+nums[i]+1)
            count+=1
            if i>=len(nums)-1:
                return count
        return count