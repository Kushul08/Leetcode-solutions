# ─────────────────────────────────────────────────
#  Problem : 4001. Aggregate Two Time Series
#  Difficulty : Medium
#  Runtime  : 110 ms
#  Memory   : 67.8 MB
#  Solved   : 2026-07-26
# ─────────────────────────────────────────────────

class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        l=0
        r=0
        n1=len(series1)
        n2=len(series2)
        ans=[]
        while l<n1 or r<n2:
            if l<n1 and r<n2:
                if series1[l][0]<series2[r][0]:
                    ans.append([series1[l][0],series1[l][1]+series2[r][1]])
                    l+=1
                elif series1[l][0]>series2[r][0]:
                    ans.append([series2[r][0],series1[l][1]+series2[r][1]])
                    r+=1
                else:
                    ans.append([series1[l][0],series1[l][1]+series2[r][1]])
                    l+=1
                    r+=1
            elif l<n1 and r>=n2:
                ans.append(series1[l])
                l+=1
            else:
                ans.append(series2[r])
                r+=1
        return ans
        