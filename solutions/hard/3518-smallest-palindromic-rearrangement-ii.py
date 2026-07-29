# ─────────────────────────────────────────────────
#  Problem : 3518. Smallest Palindromic Rearrangement II
#  Difficulty : Hard
#  Runtime  : 0 ms
#  Memory   : 19.6 MB
#  Solved   : 2026-07-29
# ─────────────────────────────────────────────────

import math
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n=len(s)
        counter=defaultdict(int)
        for ch in s:
            counter[ch]+=1
        left=''
        middle=''
        for ch in string.ascii_lowercase:
            if counter[ch]%2==1:
                middle+=ch
            left+=(counter[ch]//2)*ch
        L=len(left)

        lc=defaultdict(int)
        for ch in left:
            lc[ch]+=1

        denom=1
        for ch in lc:
            denom*=math.factorial(lc[ch])
        unique_palindromes=(math.factorial(L))/denom

        if k>unique_palindromes:
            return ""

        
        ans=''
        while L>0:
            for ch in string.ascii_lowercase:
                if ch not in lc: continue
                denominator=1
                for char in lc:
                    if char==ch:
                        denominator*=math.factorial(lc[char]-1)
                    else:
                        denominator*=math.factorial(lc[char])
                count=(math.factorial(L-1))/denominator
                if count<k: # if k==count we not take because we can't build it if we pick so
                    k-=count  
                else:
                    ans+=ch
                    lc[ch]-=1
                    if lc[ch]==0:
                        del lc[ch]
                    L-=1
                    break
        return ans+middle+ans[::-1]