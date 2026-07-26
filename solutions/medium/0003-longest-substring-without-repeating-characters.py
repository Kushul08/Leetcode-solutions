# ─────────────────────────────────────────────────
#  Problem : 0003. Longest Substring Without Repeating Characters
#  Difficulty : Medium
#  Runtime  : 38 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-07-26
# ─────────────────────────────────────────────────

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        r=0
        n=len(s)
        if n==0:
            return 0
        max_=1
        hashmap={}
        while r<n:
            while l<=r and (r-l)!=len(hashmap):
                hashmap[s[l]]-=1
                if hashmap[s[l]]==0:
                    del hashmap[s[l]]
                l+=1
            hashmap[s[r]]=hashmap.get(s[r],0)+1
            if r-l+1==len(hashmap):
                max_=max(max_,r-l+1)
            r+=1
        return max_