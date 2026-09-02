# ─────────────────────────────────────────────────
#  Problem : 0229. Majority Element II
#  Difficulty : Medium
#  Runtime  : 5 ms
#  Memory   : 13.9 MB
#  Solved   : 2026-09-02
# ─────────────────────────────────────────────────

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        num1=num2=None
        count1=count2=0

        for num in nums:
            if num==num1:
                count1+=1
            elif num==num2:
                count2+=1
            elif count1==0:
                num1=num
                count1+=1
            elif count2==0:
                num2=num
                count2+=1
            else:
                count1-=1
                count2-=1
        count1=count2=0
        for num in nums:
            if num1==num:
                count1+=1
            elif num2==num:
                count2+=1
        ans=[]
        if count1>(n/3):
            ans.append(num1)
        if count2>(n/3):
            ans.append(num2)
        return ans