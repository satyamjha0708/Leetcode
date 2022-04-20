class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
                
            else:
                d[i]+=1
                
            
            
        for key,values in d.items():
            if d[key]>2:
                d[key]=values-2
                
            elif d[key]<=2:
                d[key]=0
                
        
        
        for key,values in d.items():
            for j in range(values):
                nums.remove(key)
                
                
        
            
            
                
            
            