# ─────────────────────────────────────────────────
#  Problem : 3312. Sorted GCD Pair Queries
#  Difficulty : Hard
#  Runtime  : 659 ms
#  Memory   : 42 MB
#  Solved   : 2026-07-17
# ─────────────────────────────────────────────────

from bisect import bisect_left, bisect_right
from collections import Counter
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        freq=Counter(nums)
        G=2
        MAX=max(nums)
        divisible=[0]*(MAX+1)
        divisible[1]=len(nums)
        for g in range(G,MAX+1):
            cnt=0
            for mul in range(g,MAX+1,g):
                cnt+=freq[mul]
            divisible[g]=cnt
        pairs=[0]*(MAX+1)
        for g in range(1,MAX+1):
            div=divisible[g]
            pairs[g]=(div*(div-1))//2
        exact=pairs[::]
        for g in range(MAX,0,-1):
            for mul in range(2*g,MAX+1,g):
                exact[g]-=exact[mul]
        gcd=[0]*(MAX+1)
        for i in range(1,len(gcd)):
            gcd[i]=gcd[i-1]+exact[i]
        ans=[]
        for q in queries:
            ans.append(bisect_right(gcd,q))
        return ans