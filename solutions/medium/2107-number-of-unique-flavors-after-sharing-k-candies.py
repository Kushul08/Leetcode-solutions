# ─────────────────────────────────────────────────
#  Problem : 2107. Number of Unique Flavors After Sharing K Candies
#  Difficulty : Medium
#  Runtime  : 243 ms
#  Memory   : 25.5 MB
#  Solved   : 2026-06-09
# ─────────────────────────────────────────────────

from collections import Counter
class Solution(object):
    def shareCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        hashmap=Counter(candies)

        left=0
        right=k-1
        length=0
        for right in range(k):
            if hashmap[candies[right]]==1:
                del (hashmap[candies[right]])
                continue
            hashmap[candies[right]]-=1
        length=max(length,len(hashmap))

        for right in range(right+1,len(candies)):
            hashmap[candies[left]]=hashmap.get(candies[left],0)+1
            left+=1
            if hashmap[candies[right]]==1:
                del (hashmap[candies[right]])
                continue
            hashmap[candies[right]]-=1
            length=max(length,len(hashmap))
        return length
