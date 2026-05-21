# ─────────────────────────────────────────────────
#  Problem : 3043. Find the Length of the Longest Common Prefix
#  Difficulty : Medium
#  Runtime  : 209 ms
#  Memory   : 21.4 MB
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
        for val in arr1:
            while val not in prefix_set and val>0:
                prefix_set.add(val)
                val=val//10
        
        max_len=0
        for val in arr2:
            while val not in prefix_set and val>0:
                val=val//10
            if val>0:
                max_len=max(max_len,len(str(val)))
        return max_len