# ─────────────────────────────────────────────────
#  Problem : 1345. Jump Game IV
#  Difficulty : Hard
#  Runtime  : 186 ms
#  Memory   : 32.8 MB
#  Solved   : 2026-05-18
# ─────────────────────────────────────────────────

from collections import deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        visited=[False]*len(arr)
        visited[0]=True
        hashmap={}
        for i,num in enumerate(arr):
            if num in hashmap:
                hashmap[num].append(i)
            else:
                hashmap[num]=[i]
        queue=deque([(0,0)])

        while queue:
            index,steps=queue.popleft()
            if index==len(arr)-1:
                return steps

            if 0<=index-1 and not visited[index-1]:
                visited[index-1]=True
                queue.append((index-1,steps+1))
            if index+1<len(arr) and not visited[index+1]:
                visited[index+1]=True
                queue.append((index+1,steps+1))
            for i in (hashmap[arr[index]]):
                if not visited[i]:
                    visited[i]=True
                    queue.append((i,steps+1))
            hashmap[arr[index]].clear()
        return 0