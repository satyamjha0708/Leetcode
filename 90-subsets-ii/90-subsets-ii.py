class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def func(i,arr,n,ans,temp):
            if i==n:
                temp.sort()
                if temp[:] not in ans:
                    ans.append(temp[:])
                
                
                return 
            
            
            temp.append(arr[i])
            func(i+1,arr,n,ans,temp)
            temp.pop()
            func(i+1,arr,n,ans,temp)
            
            
            
        ans=[]
        nums.sort()
        func(0,nums,len(nums),ans,[])
        
        return ans