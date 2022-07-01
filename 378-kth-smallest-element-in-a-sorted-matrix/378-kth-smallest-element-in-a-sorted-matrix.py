class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        final=[]
        for i in matrix:
            final.extend(i)
            
        final.sort()
        return final[k-1]
        