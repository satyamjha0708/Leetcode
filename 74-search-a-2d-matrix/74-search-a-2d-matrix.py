class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix[0])
        n=len(matrix)
        low=0
        high=m*n-1
        
        
        while low<=high:
            middle=(low+high)-1//2
            
            if matrix[middle//m][middle%m]==target:
                return True
            
            
            elif target<matrix[middle//m][middle%m]:
                high=middle-1
                
                
            else:
                low=middle+1
                
                
                
        else:
            return False
        
        
        
        