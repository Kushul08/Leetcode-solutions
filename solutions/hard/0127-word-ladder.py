# ─────────────────────────────────────────────────
#  Problem : 0127. Word Ladder
#  Difficulty : Hard
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-06-04
# ─────────────────────────────────────────────────

from collections import deque, Counter
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        queue=deque()
        queue.append((beginWord,1))
        visited=set(beginWord)

        def check(s1,s2):
            count=0
            for a,b in zip(s1,s2):
                if count>1: return False
                if a!=b:
                    count+=1
            if count==1:
                return True
            return False
        ans=float('inf')
        while queue:
            # print(queue)
            node,step=queue.popleft()
            if node==endWord:
                ans=min(ans,step)
                continue
            for char in wordList:
                if char in visited:
                    continue
                if check(node,char):
                    queue.append((char,step+1))
                    # print(queue)
                    visited.add(char)
        if ans==float('inf'): return 0
        return ans