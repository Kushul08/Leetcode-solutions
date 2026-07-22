# ─────────────────────────────────────────────────
#  Problem : 3501. Maximize Active Section with Trade II
#  Difficulty : Hard
#  Runtime  : 0 ms
#  Memory   : 19.6 MB
#  Solved   : 2026-07-22
# ─────────────────────────────────────────────────

class SegmentTree:
    def __init__(self,arr):
        self.n=len(arr)
        self.arr=arr
        self.seg=[0]*(self.n<<2)

        if self.n:
            self.build(1,0,self.n-1)
    def build(self,p:int,l:int,r:int)->None:
        if l==r:
            self.seg[p]=self.arr[l]
            return
        mid=(l+r)>>1
        self.build(p<<1,l,mid)
        self.build(p<<1|1,mid+1,r)
        self.seg[p]=max(self.seg[p<<1],self.seg[p<<1|1])
    def query(self,L:int,R:int)->int:
        if L>R:
            return 0
        def _query(p:int,l:int,r:int)->int:
            if L<=l and r<=R:
                return self.seg[p]
            mid=(l+r)>>1
            res=0

            if L<=mid:
                res=max(res,_query(p<<1,l,mid))
            else:
                res=max(res,_query(p<<1|1,mid+1,r))
            return res
        return _query(1,0,self.n-1)
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n=len(s)
        count1=s.count('1')

        zero=[]
        left=[]
        right=[]
        i=0
        while i<n:
            start=i
            while i<n and s[i]==s[start]:
                i+=1
            if s[start]=='0':
                zero.append(i-start)
                left.append(start)
                right.append(i-1)
        m=len(zero)
        if m<2:
            return [count1]*len(queries)
        tempsum=[zero[i]+zero[i+1] for i in range(m-1)]
        seg=SegmentTree(tempsum)
        ans=[]

        for l,r in queries:
            i=bisect_left(right,l)
            j=bisect_right(left,r)-1

            if i>m-1 or j<0 or i>=j:
                ans.append(count1)
                continue
            firstlen=right[i]-max(left[i],l)+1
            lastlen=min(right[j],r)-left[j]+1

            if i+1==j:
                bestgain=firstlen+lastlen
                ans.append(count1+bestgain)
                continue
            val1=fistlen+zero[i+1]
            val2=zero[j-1]+lastlen
            val3=seg.query(i+1,j-2)
            bestgain=max(val1,val2,val3)
            ans.append(count1+bestgain)
        return ans