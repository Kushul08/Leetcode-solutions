# ─────────────────────────────────────────────────
#  Problem : 0045. Jump Game II
#  Difficulty : Medium
#  Runtime  : 6 ms
#  Memory   : 12.8 MB
#  Solved   : 2026-05-17
# ─────────────────────────────────────────────────

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        def find_greater(start,end):
            farthest=start
            index=start
            for i in range(start,end):
                if farthest<i+nums[i]:
                    farthest=i+nums[i]
                    index=i
            return index
        
        i=0
        count=0
        while i<len(nums):
            if nums[i]+i>=len(nums)-1:
                return count+1
            i=find_greater(i+1,i+nums[i]+1)
            count+=1
            if i>=len(nums)-1:
                return count
        return count