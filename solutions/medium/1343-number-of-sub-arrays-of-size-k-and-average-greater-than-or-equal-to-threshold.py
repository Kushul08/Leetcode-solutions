# ─────────────────────────────────────────────────
#  Problem : 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
#  Difficulty : Medium
#  Runtime  : 56 ms
#  Memory   : 19.9 MB
#  Solved   : 2026-07-21
# ─────────────────────────────────────────────────

class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        sums=0
        n=len(arr)
        count=0
        for i in range(k-1):
            sums+=arr[i]
        l=0
        r=k-1
        while r<n:
            sums+=arr[r]
            # print(sums)
            if sums/k>=threshold:
                count+=1
            sums-=arr[l]
            l+=1
            r+=1
        return count