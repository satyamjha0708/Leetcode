class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def func(idx,arr,n,ans,temp,target):
            if idx==n:
                if target==0:
                    ans.append(temp[:])
                    
                return 
                    
                    
            if arr[idx]<=target:
                temp.append(arr[idx])
                func(idx,arr,n,ans,temp,target-arr[idx])
                temp.pop()
                
            func(idx+1,arr,n,ans,temp,target)
            
            
        ans=[]
        
        func(0,candidates,len(candidates),ans,[],target)
        
        
        return ans