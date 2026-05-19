# ─────────────────────────────────────────────────
#  Problem : 2540. Minimum Common Value
#  Difficulty : Easy
#  Runtime  : 17 ms
#  Memory   : 24.2 MB
#  Solved   : 2026-05-19
# ─────────────────────────────────────────────────

class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                return nums1[i]
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return -1