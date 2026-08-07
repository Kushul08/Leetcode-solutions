# ─────────────────────────────────────────────────
#  Problem : 2035. Partition Array Into Two Arrays to Minimize Sum Difference
#  Difficulty : Hard
#  Runtime  : 1950 ms
#  Memory   : 22.3 MB
#  Solved   : 2026-08-07
# ─────────────────────────────────────────────────

from bisect import bisect_left
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n=len(nums)//2
        left=[[] for _ in range(n+1)]
        right=[[] for _ in range(n+1)]
        
        total=sum(nums)
        def recur(i,take,sums,subsets,arr):
            if i==n:
                subsets[take].append(sums)
                return
            recur(i+1,take+1,sums+arr[i],subsets,arr)
            recur(i+1,take,sums,subsets,arr)
            return
        recur(0,0,0,left,nums[:n])
        recur(0,0,0,right,nums[n:])

        min_diff=float('inf')
        for k in range(n+1):
            arr=right[n-k]
            arr.sort()
            for i in range(len(left[k])):
                l_sum=left[k][i]
                rem=total/2-l_sum
                indx=bisect_left(arr,rem)
                if indx<len(arr):
                    val=arr[indx]
                    min_diff=min(min_diff,abs(total-2*(l_sum+val)))
                if indx>0:
                    val=arr[indx-1]
                    min_diff=min(min_diff,abs(total-2*(l_sum+val)))
        return min_diff