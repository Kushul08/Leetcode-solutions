# ─────────────────────────────────────────────────
#  Problem : 3016. Minimum Number of Pushes to Type Word II
#  Difficulty : Medium
#  Runtime  : 91 ms
#  Memory   : 20.2 MB
#  Solved   : 2026-07-31
# ─────────────────────────────────────────────────

from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        hashmap=Counter(word)
        hashmap=dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        count=0
        ans=0
        for key,val in hashmap.items():
            count+=1
            if count<=8:
                ans+=val
            elif count<=16:
                ans+=(val*2)
            elif count<=24:
                ans+=(val*3)
            else:
                ans+=(val*4)
        return ans