# ─────────────────────────────────────────────────
#  Problem : 3960. Frequency Balance Subarray
#  Difficulty : Medium
#  Runtime  : 3588 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-06-14
# ─────────────────────────────────────────────────

class Solution(object):
    def getLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len=1
        for i in range(len(nums)):
            hashmap={}
            freq={}
            for j in range(i,len(nums)):
                curr=nums[j]
                if curr in hashmap:
                    old=hashmap[curr]
                    freq[old]-=1
                    if freq[old]==0:
                        del freq[old]
                hashmap[curr]=hashmap.get(curr,0)+1
                new_freq=hashmap[curr]
                freq[new_freq]=freq.get(new_freq,0)+1
                if j-i+1>=2:
                    max_freq=max(freq)
                    min_freq=min(freq)
                    if len(hashmap)==1:
                        max_len=max(max_len,j-i+1)
                    elif len(freq)==1:
                        if len(hashmap)==1:
                            max_len=max(max_len,j-i+1)
                    elif len(freq)==2:
                        if max_freq==min_freq*2:
                            max_len=max(max_len,j-i+1)
        return max_len