class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        def func(arr,matrix):
            if arr[0]>=0:
                
                for i in range(0,arr[0]):
                    matrix[i][arr[1]]=0
                    
            if arr[0]<=len(matrix):
                
                for i in range(arr[0],len(matrix)):
                    matrix[i][arr[1]]=0
                    
                    
            if arr[1]>=0:
                for i in range(0,arr[1]):
                    matrix[arr[0]][i]=0
                    
            if arr[1]<=len(matrix[0]):
                
                for i in range(arr[1],len(matrix[0])):
                    matrix[arr[0]][i]=0
                
                
                    
                    
                    
                    
                    
        l=[]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    l.append([i,j])
        print(l)
        for i in l:           
            func(i,matrix)
            
            
        return matrix
                    
                    
                    
        
        