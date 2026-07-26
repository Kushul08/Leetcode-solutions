# ─────────────────────────────────────────────────
#  Problem : 0003. Longest Substring Without Repeating Characters
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-07-26
# ─────────────────────────────────────────────────

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        r=1
        n=len(s)
        if n==0:
            return 0
        max_=1
        hashmap={s[0]:1}
        while r<n:
            while l<=r and (r-l)!=len(hashmap):
                # print(hashmap,l,r)
                hashmap[s[l]]-=1
                if hashmap[s[l]]==0:
                    del hashmap[s[l]]
                l+=1
            hashmap[s[r]]=hashmap.get(s[r],0)+1
            max_=max(max_,r-l)
            r+=1
        return max_