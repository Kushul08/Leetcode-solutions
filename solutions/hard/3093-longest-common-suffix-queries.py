# ─────────────────────────────────────────────────
#  Problem : 3093. Longest Common Suffix Queries
#  Difficulty : Hard
#  Runtime  : 0 ms
#  Memory   : 12.3 MB
#  Solved   : 2026-05-28
# ─────────────────────────────────────────────────

from heapq import heappush,heappop
import heapq
class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        """
        :type wordsContainer: List[str]
        :type wordsQuery: List[str]
        :rtype: List[int]
        """
        look={}

        for i,word in enumerate(wordsContainer):
            for j in range(len(word)+1):
                if word[j:] in look:
                    heappush(look[word[j:]],(len(word),i))
                else:
                    look[word[j:]]=[]
                    heappush(look[word[j:]],(len(word),i))
        ans=[]
        for i,word in enumerate(wordsQuery):
            for i in range(len(word)+1):
                if word[i:] in look:
                    ans.append(look[word[i:]][0][1])
                    break
        return ans