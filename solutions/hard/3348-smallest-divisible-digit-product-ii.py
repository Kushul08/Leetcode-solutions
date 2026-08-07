# ─────────────────────────────────────────────────
#  Problem : 3348. Smallest Divisible Digit Product II
#  Difficulty : Hard
#  Runtime  : 306 ms
#  Memory   : 33.8 MB
#  Solved   : 2026-08-07
# ─────────────────────────────────────────────────

from math import gcd
class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        n=len(num)
        new_t=t
        for i in range(2,10):
            while new_t%i==0:
                new_t//=i
        if new_t>1:
            return '-1'
        rem=[0]*(n+1)
        rem[0]=t
        pos=n-1

        nums=list(num)
        for i in range(n):
            if nums[i]=='0':
                pos=i
                break
            rem[i+1]=rem[i]//math.gcd(rem[i],int(num[i]))
        if rem[n]==1:
            return num
        for i in range(pos,-1,-1):
            while True:
                nums[i]=chr(ord(nums[i])+1)
                if nums[i]>'9':
                    break
                t_now=rem[i]//math.gcd(rem[i],int(nums[i]))
                k=9

                for j in range(n-1,i,-1):
                    while t_now%k!=0:
                        k-=1
                    t_now//=k
                    nums[j]=str(k)
                if t_now==1:
                    return ''.join(nums)
        ans=[]
        org_t=t
        for i in range(9,1,-1):
            while org_t%i==0:
                ans.append(str(i))
                org_t//=i
        ans_str=''.join(ans)
        padding=max(n+1-len(ans_str),0)
        ans_str+='1'*padding

        return ans_str[::-1]