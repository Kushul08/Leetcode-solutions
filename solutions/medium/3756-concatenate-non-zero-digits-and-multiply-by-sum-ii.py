# ─────────────────────────────────────────────────
#  Problem : 3756. Concatenate Non-Zero Digits and Multiply by Sum II
#  Difficulty : Medium
#  Runtime  : 12 ms
#  Memory   : 16.1 MB
#  Solved   : 2026-07-08
# ─────────────────────────────────────────────────

from bisect import bisect_left, bisect_right
class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD=int(1e9+7)
        digits=[]
        pos=[]
        pow10=[1]*(len(s)+1)
        for i in range(1,len(pow10)):
            pow10[i]=pow10[i-1]*10%MOD
        for i in range(len(s)):
            if int(s[i])!=0:
                digits.append(int(s[i]))
                pos.append(i)

        sums=[digits[0]]
        for i in range(1,len(digits)):
            sums.append(sums[-1]+digits[i])

        pref=[digit for digit in digits]
        for i in range(1,len(pref)):
            pref[i]=(pref[i-1]*10+digits[i])%MOD
        
        ans=[]
        for l,r in queries:
            start=bisect_left(pos,l)
            end=bisect_right(pos,r)-1
            if start>end:
                ans.append(0)
                continue
            n=end-start+1
            if start==0:
                req_sum=sums[end]
                x=pref[end]
            else:
                x=(pref[end]-pref[start-1]*pow10[n])%MOD
                req_sum=sums[end]-sums[start-1]
                
            ans.append(x*req_sum%MOD)
        return ans
                    