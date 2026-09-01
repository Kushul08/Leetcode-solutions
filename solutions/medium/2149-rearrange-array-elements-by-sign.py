# ─────────────────────────────────────────────────
#  Problem : 2149. Rearrange Array Elements by Sign
#  Difficulty : Medium
#  Runtime  : 149 ms
#  Memory   : 49.4 MB
#  Solved   : 2026-09-01
# ─────────────────────────────────────────────────

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positive=[]
        negative=[]
        for num in nums:
            if num<0:
                negative.append(num)
            else:
                positive.append(num)
        ans=[]
        pos=neg=0
        for i in range(len(nums)):
            if i%2==0:
                ans.append(positive[pos])
                pos+=1
            else:
                ans.append(negative[neg])
                neg+=1
        return ans