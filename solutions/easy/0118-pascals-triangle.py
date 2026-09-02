# ─────────────────────────────────────────────────
#  Problem : 0118. Pascal's Triangle
#  Difficulty : Easy
#  Runtime  : 3 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-09-02
# ─────────────────────────────────────────────────

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return [[1],[1,1]]
        elif numRows==3:
            return [[1],[1,1],[1,2,1]]
        else:
            result=[[1],[1,1],[1,2,1]]
            nums=[1,2,1]
            for j in range(3,numRows):
                small_result=[1]
                for i in range(len(nums)-1):
                    small_result.append(nums[i]+nums[i+1])
                small_result.append(1)
                result.append(small_result)
                nums=small_result
        return result


        