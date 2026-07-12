# ─────────────────────────────────────────────────
#  Problem : 1331. Rank Transform of an Array
#  Difficulty : Easy
#  Runtime  : 50 ms
#  Memory   : 27.9 MB
#  Solved   : 2026-07-12
# ─────────────────────────────────────────────────

class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        nums=sorted(set(arr))
        hashmap={}
        for i,num in enumerate(nums):
            hashmap[num]=i+1
        ans=[]
        for num in arr:
            ans.append(hashmap[num])
        return ans