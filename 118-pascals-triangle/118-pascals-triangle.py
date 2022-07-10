class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for i in range(numRows):
            ans.append([0]*(i+1))
            ans[i][0]=1
            ans[i][i]=1
            
            for j in range(1,i):
                ans[i][j]=ans[i-1][j-1] + ans[i-1][j]
                
                
        return ans