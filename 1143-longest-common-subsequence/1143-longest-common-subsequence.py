class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def func(text1,text2,idx1,idx2,dp):
            if idx1<0 or idx2<0:
                return 0
            
            if dp[idx1][idx2]!=-1:
                return dp[idx1][idx2]
            
            
            if text1[idx1]==text2[idx2]:
                dp[idx1][idx2]= 1+func(text1,text2,idx1-1,idx2-1,dp)
                return dp[idx1][idx2]
            
            else:
                dp[idx1][idx2]=max(func(text1,text2,idx1-1,idx2,dp),func(text1,text2,idx1,idx2-1,dp))
                return dp[idx1][idx2]
            
         
        dp=[[-1 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
      
            
        return func(text1,text2,len(text1)-1,len(text2)-1,dp)
        
    
    
    
    
        