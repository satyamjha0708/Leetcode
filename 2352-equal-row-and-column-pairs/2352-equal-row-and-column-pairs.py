class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        col=[]
        
        for i in range(len(grid[0])):
                l=[]
                for j in grid:
                    l.append(j[i])
                
                col.append(l)
               
        print(col)
        cnt=0       
        for i in grid:
                cnt+=col.count(i)
                        
                        
                        
        return cnt