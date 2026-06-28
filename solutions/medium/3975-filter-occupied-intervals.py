# ─────────────────────────────────────────────────
#  Problem : 3975. Filter Occupied Intervals
#  Difficulty : Medium
#  Runtime  : 259 ms
#  Memory   : 41.3 MB
#  Solved   : 2026-06-28
# ─────────────────────────────────────────────────

class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        occupiedIntervals.append([freeStart,freeEnd])
        occupiedIntervals.sort()
        stack=[]

        for a,b in occupiedIntervals :
            if stack and stack[-1][-1]>=a:
                stack[-1][-1]=max(stack[-1][-1],b)
            elif stack and stack[-1][-1]+1==a:
                stack[-1][-1]=max(stack[-1][-1],b)
            else:
                stack.append([a,b])

        ans=[]
        for i in range(len(stack)):
            if stack[i][0]<=freeStart and freeEnd<=stack[i][1]:
                if stack[i]==[freeStart,freeEnd]:
                    stack.pop(i)
                    break
                elif stack[i][0]==freeStart and freeEnd<stack[i][1]:
                    stack[i][0]=freeEnd+1
                elif stack[i][0]<freeStart and freeEnd==stack[i][1]:
                    stack[i][1]=freeStart-1
                else:
                    temp=[freeEnd+1,stack[i][1]]
                    stack[i][1]=freeStart-1
                    stack.insert(i+1,temp)
                break
        return stack