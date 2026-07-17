# ─────────────────────────────────────────────────
#  Problem : 3312. Sorted GCD Pair Queries
#  Difficulty : Hard
#  Runtime  : 1107 ms
#  Memory   : 51.5 MB
#  Solved   : 2026-07-17
# ─────────────────────────────────────────────────

from bisect import bisect_left, bisect_right
from collections import Counter
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        freq=Counter(nums)
        # print(freq)
        G=2
        MAX=max(nums)
        divisible={1:len(nums)}
        for g in range(G,MAX+1):
            cnt=0
            for mul in range(g,MAX+1,g):
                cnt+=freq[mul]
            divisible[g]=cnt
        # print(divisible)
        pairs={}
        for g in range(1,MAX+1):
            div=divisible[g]
            pairs[g]=(div*(div-1))//2
        exact=pairs.copy()
        # inclusion-exclusion (or Möbius-style sieve) step.
        for g in range(MAX,0,-1):
            for mul in range(2*g,MAX+1,g):
                exact[g]-=exact.get(mul,0)
        # print(exact)
        gcd=[0]*(MAX+1)
        for i in range(1,len(gcd)):
            gcd[i]=gcd[i-1]+exact[i]
        # print(gcd)
        ans=[]
        for q in queries:
            ans.append(bisect_right(gcd,q))
        return ans