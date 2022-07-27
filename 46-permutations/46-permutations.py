class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def func(ans,arr,index):
            if index==len(arr):
                ans.append(arr[:])
                return 
            
            
            for i in range(index,len(arr)):
                arr[i],arr[index]=arr[index],arr[i]
                func(ans,arr,index+1)
                arr[index],arr[i]=arr[i],arr[index]
                
        ans=[]    
        func(ans,nums,0)    
        return ans
        