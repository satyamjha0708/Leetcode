class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans=[]
        
        
        for j in range(len(matrix[0])):
            l=[]
            for i in range(len(matrix)):
                l.append(matrix[i][j])
                
                
            ans.append(l)
            
            
        return ans