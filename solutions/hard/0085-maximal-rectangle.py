# ─────────────────────────────────────────────────
#  Problem : 0085. Maximal Rectangle
#  Difficulty : Hard
#  Runtime  : 34 ms
#  Memory   : 24.7 MB
#  Solved   : 2026-08-31
# ─────────────────────────────────────────────────

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n,m=len(matrix),len(matrix[0])
        def area(nums):
            stack=[]
            ans=0
            for i in range(m):
                while stack and nums[stack[-1]]>nums[i]:
                    indx=stack.pop() # for this the current is nse and top of stack is pse
                    pse=stack[-1] if stack else -1
                    ans=max(ans,nums[indx]*(i-pse-1))
                stack.append(i)
            nse=m
            while stack:
                indx=stack.pop()
                pse=stack[-1] if stack else -1
                ans=max(ans,nums[indx]*(nse-pse-1))
            return ans
        histos=[0]*(m)
        max_area=0
        def help(nums,histos):
            for i in range(len(nums)):
                if nums[i]=='1':
                    histos[i]+=1
                else:
                    histos[i]=0
            return histos
        for i in range(n):
            histos=help(matrix[i],histos)
            max_area=max(max_area,area(histos))
        return max_area