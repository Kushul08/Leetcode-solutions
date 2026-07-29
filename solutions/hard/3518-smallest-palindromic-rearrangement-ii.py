# ─────────────────────────────────────────────────
#  Problem : 3518. Smallest Palindromic Rearrangement II
#  Difficulty : Hard
#  Runtime  : 342 ms
#  Memory   : 19.8 MB
#  Solved   : 2026-07-29
# ─────────────────────────────────────────────────

from math import gcd, factorial
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:

        def nCr(n, r, limit):
            r = min(r, n - r)

            ans = 1

            for i in range(1, r + 1):
                num = n - r + i
                den = i

                g = gcd(num, den)
                num //= g
                den //= g

                g = gcd(ans, den)
                ans //= g
                den //= g

                ans *= num

                if den != 1:
                    ans //= den

                if ans > limit:
                    return limit + 1

            return ans

        def count(freq, total, limit):
            ans = 1
            remaining = total

            for f in freq.values():

                if f == 0:
                    continue

                ways = nCr(remaining, f, limit)

                ans *= ways

                if ans > limit:
                    return limit + 1

                remaining -= f

            return ans
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

        if count(lc, L, k) < k:
            return ""
        

        
        # denominator=1
        # for char in lc:
            # denominator*=fact[lc[char]]
        
        ans=''
        while L>0:
            for ch in string.ascii_lowercase:
                if ch not in lc: continue
                # denominator=1
                # for char in lc:
                #     if char==ch:
                #         denominator*=math.factorial(lc[char]-1)
                #     else:
                #         denominator*=math.factorial(lc[char])
                # new=denominator//lc[ch]
                # count=fact[L-1]//new
                lc[ch]-=1
                if lc[ch]==0:
                    del lc[ch]
                cnt=count(lc,L-1,k)
                if cnt<k: # if k==count we not take because we can't build it if we pick so
                    k-=cnt  
                    lc[ch]=lc.get(ch,0)+1
                else:
                    ans+=ch
                    L-=1
                    break
        return ans+middle+ans[::-1]