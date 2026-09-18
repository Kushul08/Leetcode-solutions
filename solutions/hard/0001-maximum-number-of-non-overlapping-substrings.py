# ─────────────────────────────────────────────────
#  Problem : 0001. Maximum Number of Non-Overlapping Substrings
#  Difficulty : Hard
#  Runtime  : 0 ms
#  Memory   : 19.5 MB
#  Solved   : 2026-09-18
# ─────────────────────────────────────────────────

from collections import Counter
class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        
        start=[-1]*26
        end=[-1]*26
        hashmap=Counter(s)
        for i,ch in enumerate(s):
            if start[ord(ch)-97]==-1:
                start[ord(ch)-97]=i
                end[ord(ch)-97]=i
            end[ord(ch)-97]=i
        nums=[]
        for ch in hashmap:
            nums.append([start[ord(ch)-97],end[ord(ch)-97]])
        nums.sort(key=lambda item:item[1])

        prev=-1
        ans=[]
        for first,second in nums:
            if first>prev:
                string=s[first:second+1]
                ans.append(string)
                prev=second
        return ans