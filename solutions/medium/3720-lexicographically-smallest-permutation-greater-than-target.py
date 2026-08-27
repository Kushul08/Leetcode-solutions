# ─────────────────────────────────────────────────
#  Problem : 3720. Lexicographically Smallest Permutation Greater Than Target
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-08-27
# ─────────────────────────────────────────────────

class Solution(object):
    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n=len(s)
        nums=[0]*(27)
        for ch in s:
            nums[ord(ch)-97]+=1
        j=0
        ans=''
        while j<n:
            for i in range(27):
                if nums[i]!=0 and 97+i==ord(target[j]):
                    ans+=chr(i+97)
                    j+=1
                    nums[i]-=1
                    break
                elif nums[i]!=0 and 97+i>ord(target[j]):
                    ans+=chr(i+97)
                    j+=1
                    nums[i]-=1
                    chars=''
                    for k in range(27):
                        if nums[k]!=0:
                            chars+=chr(k+97)*nums[k]            
                    return ans+chars
            if i==26: return ''
        if ans>target:
            return ans
        j=n
        while j>0:
            j-=1

            nums[ord(target[j])-97]+=1

            for i in range(ord(target[j])-96,26):
                if nums[i]>0:
                    chars=''
                    nums[i]-=1
                    for k in range(26):
                        if nums[k]>0:
                            chars+=chr(k+97)*nums[k]
                    return target[:j]+chr(i+97)+chars
        return ''