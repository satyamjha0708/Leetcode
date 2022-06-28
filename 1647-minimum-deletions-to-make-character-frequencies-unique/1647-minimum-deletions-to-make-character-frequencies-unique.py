class Solution:
    def minDeletions(self, s: str) -> int:
        d={}
        for i in s:
            if i not in d:
                d[i]=1
                
            else:
                d[i]+=1
                
                
        ans=[]
        for values in d.values():
            ans.append(values)
            
            
        ans.sort()
        
        n=len(ans)
        i=1
        count=0
        
        while i<n:
            if ans[i-1]!=0 and ans[i]==ans[i-1]:
                ans[i-1]-=1
                i=0
                count+=1
                
            else:
                i+=1
                
                
        
        return count
            
        