# ─────────────────────────────────────────────────
#  Problem : 3838. Weighted Word Mapping
#  Difficulty : Easy
#  Runtime  : 20 ms
#  Memory   : 12.3 MB
#  Solved   : 2026-06-13
# ─────────────────────────────────────────────────

class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        res=''
        for word in words:
            sums=0
            for i in range(len(word)):
                index=ord(word[i])-97
                sums+=weights[index]
            num=sums%26
            res+=(chr(122-num))
        return res