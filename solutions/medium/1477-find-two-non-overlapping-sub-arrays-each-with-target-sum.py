# ─────────────────────────────────────────────────
#  Problem : 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-09-17
# ─────────────────────────────────────────────────

class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n=len(arr)
        min1=-1
        min2=-1
        i=0
        while i<n:
            sums=0
            for j in range(i,n):
                sums+=arr[j] 
                if sums==target:
                    length=(j-i+1)
                    if min1==-1:
                        min1=length
                    elif min2==-1:
                        min2=length
                    else:
                        if min1>length:
                            min1=length
                        elif min2>length:
                            min2=length
                    i=j
                    break
                elif sums>target:
                    break
            i+=1
        if min1!=-1 and min2!=-1:
            return min1+min2
        return -1