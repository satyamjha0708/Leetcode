class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        global dp
        dp=[0]*len(arr)
        
        def helper(arr,index,d):
                if dp[index]>0:
                        return dp[index]
                res=0
                
                for i in range(index-1,max(-1,index-d-1),-1):
                        if arr[index]<=arr[i]:break
                        res=max(res,helper(arr,i,d))
                                
                                
                for j in range(index+1,min(len(arr),index+d+1)):
                        if arr[index]<=arr[j]:break
                                
                        res=max(res,helper(arr,j,d))
                        
                        
                dp[index]=res+1
                
                                
                return dp[index]
        
        return max(helper(arr,i,d) for i in range(len(arr)))
        
        
        
        