# ─────────────────────────────────────────────────
#  Problem : 2213. Longest Substring of One Repeating Character
#  Difficulty : Hard
#  Runtime  : 6132 ms
#  Memory   : 108.5 MB
#  Solved   : 2026-08-13
# ─────────────────────────────────────────────────

class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        n=len(s)
        pre=[0]*(4*n)
        suf=[0]*(4*n)
        maxlen=[0]*(4*n)
        leftchar=['']*(4*n)
        rightchar=['']*(4*n)

        def pushup(u,l,r):
            mid=(l+r)>>1
            leftlen=mid-l+1
            rightlen=r-mid
            left=u<<1
            right=u<<1|1
            leftchar[u]=leftchar[left]
            rightchar[u]=rightchar[right]
            pre[u]=pre[left]
            if pre[left]==leftlen and rightchar[left]==leftchar[right]:
                pre[u]=pre[left]+pre[right]
            suf[u]=suf[right]
            if suf[right]==rightlen and rightchar[left]==leftchar[right]:
                suf[u]=suf[right]+suf[left]
            maxlen[u]=max(maxlen[left],maxlen[right])
            if rightchar[left]==leftchar[right]:
                maxlen[u]=max(maxlen[u],suf[left]+pre[right])
                
        def build(u,l,r):
            if l==r:
                pre[u]=1
                suf[u]=1
                maxlen[u]=1
                leftchar[u]=s[l]
                rightchar[u]=s[l]
                return
            mid=(l+r)>>1
            build(u<<1,l,mid)
            build(u<<1 |1,mid+1,r)
            pushup(u,l,r)
        
        def update(u,l,r,pos,ch):
            if l==r:
                leftchar[u]=ch
                rightchar[u]=ch
                return
            mid=(l+r)>>1
            if pos<=mid:
                update(u<<1,l,mid,pos,ch)
            else:
                update(u<<1|1,mid+1,r,pos,ch)
            pushup(u,l,r)
        build(1,0,n-1)
        k=len(queryIndices)
        ans=[]
        for i in range(k):
            update(1,0,n-1,queryIndices[i],queryCharacters[i])
            ans.append(maxlen[1])
        return ans