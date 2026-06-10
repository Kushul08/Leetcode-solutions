# ─────────────────────────────────────────────────
#  Problem : 3691. Maximum Total Subarray Value II
#  Difficulty : Hard
#  Runtime  : 3233 ms
#  Memory   : 51.7 MB
#  Solved   : 2026-06-10
# ─────────────────────────────────────────────────

import heapq
from math import log2
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n=len(nums)
        heap=[]
        K=n.bit_length()
        print(K)
        stMax=[[0]*K for _ in range(n)]
        stMin=[[0]*K for _ in range(n)]

        for i in range(n):
            stMax[i][0]=stMin[i][0]=nums[i]
        for j in range(1,K):
            step=1<<(j-1)
            for i in range(n-(1<<j)+1):
                stMax[i][j]=max(stMax[i][j-1],stMax[i+step][j-1])
                stMin[i][j]=min(stMin[i][j-1],stMin[i+step][j-1])
        def queryMax(l:int,r:int)->int:
            j=(r-l+1).bit_length()-1
            return max(stMax[l][j],stMax[r-(1<<j)+1][j])
        def queryMin(l:int,r:int)->int:
            j=(r-l+1).bit_length()-1
            return min(stMin[l][j],stMin[r-(1<<j)+1][j])
        pq=[
            (-(queryMax(l,n-1)-queryMin(l,n-1)),l,n-1)
            for l in range(n)
        ]

        heapq.heapify(pq)
        ans=0
        while k:
            negVal,l,r=heapq.heappop(pq)
            ans-=negVal
            k-=1
            if r>l:
                heapq.heappush(
                    pq,(-(queryMax(l,r-1)-queryMin(l,r-1)),l,r-1)
                    )
    
        return ans