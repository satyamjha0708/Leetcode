class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        ans=0
        visit=[[0]*m for i in range(n)]
        cnt=0
        
        queue=[]
        
        for i in range(n):
                for j in range(m):
                        if grid[i][j]==2:
                                queue.append([[i,j],0])
                                visit[i][j]=2
                                
                                
                        
                        else:
                                visit[i][j]=0
                                
                                
                        
                        if grid[i][j]==1:
                                cnt+=1
                                
                

                                
        drow=[-1,0,1,0]
        dcol=[0,1,0,-1]
        cnt1=0
        
        
        while queue:
                x=queue.pop(0)
                row=x[0][0]
                col=x[0][1]
                t=x[1]
                
                ans=max(t,ans)
                
                
                for i in range(4):
                        nrow=row+drow[i]
                        ncol=col+dcol[i]
                        
                        
                        if nrow>=0 and nrow<n and ncol>=0 and ncol<m and visit[nrow][ncol]==0 and grid[nrow][ncol]==1:
                                queue.append([[nrow,ncol],t+1])
                                
                                visit[nrow][ncol]=2
                                cnt1+=1
                                
        if cnt1!=cnt:
                return -1
                
        return ans
        
                                
        
        