class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def func1(arr,nums):
                for i in range(len(arr)):
                        if arr[i]>0:
                                arr[i]=arr[i]-nums
                        
                        
                return arr
        
        
        
        def func(arr):
                heap=[]
                for i in arr:
                        if i>0:
                                heap.append(i)
                                
                if len(heap)>0:
                        return min(heap)
                else:
                        return 0
                
                
        op=0        
        while sum(nums)!=0:
                op+=1
                x=func(nums)
                nums=func1(nums,x)
                
                
                
        return op