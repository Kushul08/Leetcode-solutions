# ─────────────────────────────────────────────────
#  Problem : 1520. Maximum Number of Non-Overlapping Substrings
#  Difficulty : Hard
#  Runtime  : 277 ms
#  Memory   : 20.8 MB
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
        def getinterval(ch):
            l=start[ord(ch)-97]
            e=end[ord(ch)-97]
            curr=l

            while curr<e:
                char=s[curr]
                if start[ord(char)-97]<l:
                    return None
                e=max(e,end[ord(char)-97])
                curr+=1
            return (l,e)
        intervals=[]
        for ch in hashmap:
            interval=getinterval(ch)
            if interval:
                intervals.append(interval)
        intervals.sort(key=lambda item:item[1])

        prev=-1
        ans=[]
        for first,second in intervals:
            if first>prev:
                string=s[first:second+1]
                ans.append(string)
                prev=second
        return ans