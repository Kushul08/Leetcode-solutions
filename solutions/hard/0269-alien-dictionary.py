# ─────────────────────────────────────────────────
#  Problem : 0269. Alien Dictionary
#  Difficulty : Hard
#  Runtime  : 1 ms
#  Memory   : 12.3 MB
#  Solved   : 2026-06-18
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        all_chars=set()
        adj_list={}
        for word in words:
            for char in word:
                all_chars.add(char)
        for i in range(len(words)-1):
            word1=words[i]
            word2=words[i+1]
            if len(word1)>len(word2) and word1.startswith(word2):
                return ''
            for i,j in zip(word1,word2):
                if i!=j:
                    if i in adj_list:
                        adj_list[i].append(j)
                    else:
                        adj_list[i]=[j]
                    break
            
        
        def toposort(graph):
            in_degree={}
            queue=deque()
            stack=[]

            for key,val in graph.items():
                for node in val:
                    in_degree[node]=in_degree.get(node,0)+1
            for char in all_chars:
                if char not in in_degree:
                    in_degree[char]=0

            for char in in_degree:
                if in_degree[char]==0:
                    queue.append(char)
            # print(queue)

            while queue:
                node=queue.popleft()
                stack.append(node)
                if node not in graph: continue
                for neigh in graph[node]:
                    in_degree[neigh]-=1
                    if in_degree[neigh]==0:
                        queue.append(neigh)
            if len(stack)!=len(all_chars):
                return ''
            return stack
                    
        

        
        next_word=toposort(adj_list)
        ans=''
        for word in next_word:
            ans+=word
        return ans