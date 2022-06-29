
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited={}
        row=len(grid1)
        col=len(grid1[0])
        def bfs(i,j):
            q=[]
            q.append([i,j])
            arr=[]
            arr.append([i,j])
            
            direc=[[0,1],[1,0],[-1,0],[0,-1]]
            
            while q:
                m,n=q.pop(0)
                
                for k in direc:
                    u= m+ k[0]
                    v= n+ k[1]


                    if 0<=u<row and 0<=v<col and visited.get((u,v),None) is None  and grid2[u][v]==1 :
                        visited[(u,v)]=1
                        arr.append([u,v])
                        q.append([u,v])
                        
                        
            for x,y in arr:
                if grid1[x][y]==0:
                    return False
            else:
                return True
            
            
        
        res=0
        for i in range(row):
            for j in range(col):
                if grid2[i][j]==1 and visited.get((i,j),None) is None:
                    visited[(i,j)]=1
                    if bfs(i,j):
                        res+=1
                        
                        
        return res
                