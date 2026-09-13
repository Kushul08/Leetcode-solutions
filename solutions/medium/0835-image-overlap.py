# ─────────────────────────────────────────────────
#  Problem : 0835. Image Overlap
#  Difficulty : Medium
#  Runtime  : 370 ms
#  Memory   : 12.8 MB
#  Solved   : 2026-09-13
# ─────────────────────────────────────────────────

class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        
        hashmap=defaultdict(int)
        def help(mat):
            res=[]
            for i in range(len(mat)):
                for j in range(len(mat[i])):
                    if mat[i][j]==1:
                        res.append((i,j))
            return res
        
        img_1=help(img1)
        img_2=help(img2)
        
        max_overlap=0
        for x1,y1 in img_1:
            for x2,y2 in img_2:
                vec=(x2-x1,y2-y1)
                hashmap[vec]+=1
                max_overlap=max(max_overlap,hashmap[vec])
        return max_overlap