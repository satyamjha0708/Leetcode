class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    res = self.backtrack(board,m,n,i,j,word[1:])
                    if res:
                        return True
        return False
        
        
    def backtrack(self, board,m,n, i, j, target):
        temp = board[i][j]
        if len(target) == 0:
            return True
        board[i][j] = '#'
        for x,y in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
            if 0<=x<m and 0<=y<n and target[0] == board[x][y]:
                dec = self.backtrack(board,m,n,x,y,target[1:])
                if dec:
                    return True
        board[i][j] = temp
        return False

        