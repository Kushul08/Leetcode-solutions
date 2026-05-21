# ─────────────────────────────────────────────────
#  Problem : 3043. Find the Length of the Longest Common Prefix
#  Difficulty : Medium
#  Runtime  : 493 ms
#  Memory   : 24.1 MB
#  Solved   : 2026-05-21
# ─────────────────────────────────────────────────

class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        prefix_set=set()
        for num in arr1:
            nums=str(num)
            for i in range(1,len(nums)+1):
                if nums[:i] not in prefix_set:
                    prefix_set.add(nums[:i])
        
        max_len=0
        for num in arr2:
            nums=str(num)
            count=0
            for i in range(1,len(nums)+1):
                if nums[:i] in prefix_set:
                    count+=1
            max_len=max(max_len,count)
        return max_len