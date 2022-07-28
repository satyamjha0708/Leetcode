class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def safe(row, col , board,n):
            r=row
            c=col
            
            while row>=0 and col>=0 :
                if board[row][col]=='Q':
                    return False
                row-=1
                col-=1
                
                
            row=r
            col=c
            while col>=0:
                if board[row][col]=='Q':
                    return False
                
                col-=1
                
                
            
            row=r
            col=c
            
            while row<n and col>=0:
                if board[row][col]=='Q':
                    return False
                
                row+=1
                col-=1
                
                
                
                
                
                
            return True
        
        
        
        
        def func(col,board,ans,n):
            if col==n:
                ans.append(["".join(i) for i in board])
                return 
            
            
            for row in range(n):
                if safe(row,col,board,n):
                    board[row][col]='Q'
                    func(col+1,board,ans,n)
                    board[row][col]='.'
                    
                    
            
            
        ans=[]   
        board = [["." for i in range(n)] for i in range(n)]
            
            
            
        func(0,board,ans,n)
        return ans